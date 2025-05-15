from flask import Flask, request, jsonify
from flask_cors import CORS
from analise_ia import analisar_redacao
import logging

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.DEBUG)

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        image_file = request.files.get('image')
        if not image_file:
            return jsonify({"error": "Nenhuma imagem enviada"}), 400
        
        # Processar imagem com OCR (pytesseract) para extrair texto
        # texto_extraido = ...

        # Para teste, usar texto fixo
        texto_extraido = "Texto de exemplo para análise"

        analise = analisar_redacao(texto_extraido)
        return jsonify(analise), 200

    except Exception as e:
        app.logger.error(f"Erro no upload: {e}")
        return jsonify({"error": "Erro interno no servidor", "message": str(e)}), 500

@app.route('/analyze/<id>')
def analyze(id):
    # Recuperar texto salvo por id e analisar
    pass

@app.route('/')
def home():
    return "API Correção de Redações com IA funcionando"

if __name__ == '__main__':
    app.run(debug=True)

