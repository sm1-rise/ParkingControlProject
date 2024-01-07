import cv2
import pytesseract

#Fazendo a leitura da imagem
img = cv2.imread("D:\\EstacionamentoProjeto\\OCR\\bomdia.png")

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

resultado =  pytesseract.image_to_string(img)

print(resultado)
