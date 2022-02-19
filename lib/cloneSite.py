import os, csv, shutil, re
import urllib.request
from time import sleep
from random import randint
from bs4 import BeautifulSoup

def clone():
    print(' '*10,'\033[31mATENÇÃO!\033[m Somente o HTML será clonado. O site pode não importar o \033[36mCSS\033[m\n')
    url = input('Alvo do Clone: ').lower().strip()
    url = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

    codigoCorpoPage = urllib.request.urlopen(url)
    soup = BeautifulSoup(codigoCorpoPage, features="html5lib")

    titleSite = soup.title.string
    nameDir="".join(c for c in titleSite if c.isalnum())

    criarPage = open('index.html', 'w', encoding='utf-8')
    criarPage.write(str(soup))
    criarPage.close()


    try:
        diretorio = nameDir.removeprefix('https://').removesuffix('.com')
        os.mkdir(diretorio)
        
        shutil.copy2('index.html', diretorio)
        os.remove('index.html')
        print('\033[32mSucesso!\033[m')
        sleep(1)
        print(f'Verifique o arquivo \033[33mindex.html\033[m no diretorio \033[35m{diretorio}\033[m.')
        sleep(5)

    except FileExistsError as error:
        print('\033[31mErro!\033[m O Diretório \033[35m{}\033[m já existe'.format(diretorio))
        sleep(1)
        print('Criando um novo diretório...')
        diretorio = nameDir.removeprefix('https://').removesuffix('.com')
        os.mkdir(f'{diretorio}_{randint(0, 10)}')
        os.remove('index.html')
        print(f'Verifique o arquivo \033[33mindex.html\033[m no diretorio \033[35m{diretorio}\033[m.')