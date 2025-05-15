import cv2
from PIL import Image
import pytesseract
import numpy as np

def preprocessar_imagem(caminho_imagem):
    # Carrega a imagem em escala de cinza
    imagem = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)

    # Aplica binarização (limiarização) para deixar texto em preto e fundo branco
    _, imagem_binaria = cv2.threshold(imagem, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Remove ruídos com filtro de mediana
    imagem_suavizada = cv2.medianBlur(imagem_binaria, 3)

    # Opcional: aumentar contraste
    alfa = 1.5  # Contraste
    beta = 0    # Brilho
    imagem_contraste = cv2.convertScaleAbs(imagem_suavizada, alpha=alfa, beta=beta)

    return imagem_contraste

def extrair_texto_ocr(caminho_imagem):
    imagem_processada = preprocessar_imagem(caminho_imagem)

    # Converter para PIL Image para usar pytesseract
    imagem_pil = Image.fromarray(imagem_processada)

    # Extrair texto com pytesseract (idioma português)
    texto = pytesseract.image_to_string(imagem_pil, lang='por')

    return texto

if __name__ == "__main__":
    caminho = input("Digite o caminho da imagem para teste OCR: ")
    texto_extraido = extrair_texto_ocr(caminho)
    print("=== Texto extraído pelo OCR após pré-processamento ===")
    print(texto_extraido)

    if texto_extraido.strip() == "":
        print("Aviso: Nenhum texto foi extraído. Tente melhorar a qualidade da imagem ou ajustar os parâmetros.")

