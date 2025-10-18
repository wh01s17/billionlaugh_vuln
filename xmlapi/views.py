from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lxml import etree

@csrf_exempt
def parse_xml(request):
    if request.method == 'POST':
        try:
            body = request.body.decode('utf-8')
            parser = etree.XMLParser(
                # Permite resolver entidades externas/internas
                resolve_entities=True,

                # No prohibe conexiones (para XXE completo)
                no_network=False,

                # Ignora límites de tamaño
                huge_tree=True
            )
            root = etree.fromstring(body.encode(), parser)
            return HttpResponse(f"Parseado exitoso: {etree.tostring(root).decode()}")
        except Exception as e:
            return HttpResponse(f"Error de parsing: {str(e)}", status=400)
    return HttpResponse("Usa POST con datos XML")
