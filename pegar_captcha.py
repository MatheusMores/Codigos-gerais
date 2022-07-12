import requests
import io
import pytesseract
import re
from PIL import Image
import urllib.parse
import sys
import cv2

global captcha
global cookie

def pegarCaptcha():
    headers = {
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,ru;q=0.5,mk;q=0.4',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': "PHPSESSID=f9801e78bf48c07a1bfd145f93b07440",
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    response = requests.get(
        'https://iss.londrina.pr.gov.br/images/imagem.php', headers=headers)

    img = Image.open(io.BytesIO(response.content))

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\MatheusMores\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img)

    global captcha
    captcha = re.sub('[^0-9]', '', text)  # list(counter.keys())[-1]
    print(captcha)
    return captcha

def main():
    pegarCaptcha()

main()