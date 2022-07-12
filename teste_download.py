import requests
import os 

def baixar_arquivos(url, endereco):  
    # Requisição ao servidor
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(response.content)
        print("Donwload finalizado. Salvo em: {}".format(endereco))
    else:
        response.raise_for_status() # metodo da biblioteca caso de erro no donwload
    
def main():
    BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'

    for i in range(1, 6):
        # Criar pastas
        os.mkdir(r'C:\Users\MatheusMores\Desktop\{}'.format(i))
        OUTPUT_DIR = r'C:\Users\MatheusMores\Desktop\{}'.format(i)
        # Baixar arquivo
        nome_arquivo = os.path.join(OUTPUT_DIR, 'nota_de_aula_{}.pdf'.format(i))
        baixar_arquivos(BASE_URL.format(i), nome_arquivo)

main()