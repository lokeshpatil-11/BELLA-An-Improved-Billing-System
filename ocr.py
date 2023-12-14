from PIL import Image

import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

img = Image.open('t1.png')
text = tess.image_to_string(img)

print(text)