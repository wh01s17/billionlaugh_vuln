from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import ctypes.util
import os


# Patchear la constante de amplificación de entidades en tiempo de ejecución
def allow_large_entity_expansion():
    try:
        # Localizar libxml2 dinámicamente
        libxml2_path = ctypes.util.find_library('xml2')
        if not libxml2_path:
            raise ImportError("No se encontró libxml2.")

        libxml2 = ctypes.CDLL(libxml2_path)
        
        # Obtener puntero a XML_DEFAULT_MAX_AMPL
        max_ampl_ptr = ctypes.c_void_p.in_dll(libxml2, "xmlParserMaxAmplificationFactor")
        # Asignar nuevo valor alto (por ejemplo: 1 millón)
        new_limit = 1_000_000
        ctypes.memmove(max_ampl_ptr, ctypes.byref(ctypes.c_int(new_limit)), ctypes.sizeof(ctypes.c_int))
        print(f"[+] Se cambió max amplification factor a {new_limit}")
    except Exception as e:
        print("[!] No se pudo modificar la constante:", str(e))


allow_large_entity_expansion()

from lxml import etree


@csrf_exempt
def parse_xml(request):
    if request.method == 'POST':
        try:
            body = request.body.decode('utf-8').strip()
            parser = etree.XMLParser(
                resolve_entities=True,
                no_network=False,
                huge_tree=True,
                strip_cdata=False
            )
            root = etree.fromstring(body.encode(), parser)
            return HttpResponse(etree.tostring(root, pretty_print=True).decode())
        except Exception as e:
            return HttpResponse(f"Error de parsing: {str(e)}", status=400)
    return HttpResponse("Usa POST con datos XML")