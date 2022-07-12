import requests
import os 
    

BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_1_Notes.pdf'


    # Criar pastas
os.mkdir(r'C:\Users\MatheusMores\Desktop\1')
OUTPUT_DIR = r'C:\Users\MatheusMores\Desktop\1'
# Baixar arquivo
nome_arquivo = os.path.join(OUTPUT_DIR, 'nota_de_aula_1.pdf')
response = requests.get(BASE_URL)
if response.status_code == requests.codes.OK:
    with open(nome_arquivo, 'wb') as novo_arquivo:
        novo_arquivo.write(response.content)
    print("Donwload finalizado. Salvo em: {}".format(nome_arquivo))
else:
    response.raise_for_status()
