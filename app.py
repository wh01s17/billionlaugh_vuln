from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def upload_xml():
    try:
        raw_data = request.data.decode('utf-8')

        # Parser sin protecciones -> ENTIDADES EXPANDIDAS
        parser = etree.XMLParser(
            resolve_entities=True,       # Habilitamos expansión
            no_network=False,            # No bloqueamos red
            huge_tree=True               # Árboles grandes permitidos
        )

        root = etree.fromstring(raw_data.encode(), parser)

        # Extraer texto del elemento raíz para ver expansión
        expanded_text = root.text or ''.join(root.itertext())
        response = {
            "characterCount": len(expanded_text),
            "samplePreview": expanded_text[:500]  # Mostrar primeros 500 carácteres
        }

        return response, 200
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)