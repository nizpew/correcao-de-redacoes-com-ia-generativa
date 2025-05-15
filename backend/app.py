from flask import Flask, request, jsonify
from flask_cors import CORS
from analise_ia import analisar_redacao
from PIL import Image
import pytesseract
import io

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "Nenhuma imagem enviada"}), 400

    image_file = request.files['image']
    image_bytes = image_file.read()
    image = Image.open(io.BytesIO(image_bytes))

    texto_extraido = pytesseract.image_to_string(image, lang='por')
    analise = analisar_redacao(texto_extraido)

    return jsonify(analise)

if __name__ == '__main__':
    app.run(debug=True)

