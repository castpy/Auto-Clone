import os, csv, shutil
import urllib.request
from time import sleep
from bs4 import BeautifulSoup
from lib import clear


while True:
    clear.cls()
    print('''\033[32m
 _______          _________ _______      _______  _        _______  _        _______
(  ___  )|\     /|\__   __/(  ___  )    (  ____ \( \      (  ___  )( (    /|(  ____ 
| (   ) || )   ( |   ) (   | (   ) |    | (    \/| (      | (   ) ||  \  ( || (    \/
| (___) || |   | |   | |   | |   | |    | |      | |      | |   | ||   \ | || (__
|  ___  || |   | |   | |   | |   | |    | |      | |      | |   | || (\ \) ||  __)
| (   ) || |   | |   | |   | |   | |    | |      | |      | |   | || | \   || (
| )   ( || (___) |   | |   | (___) |    | (____/\| (____/\| (___) || )  \  || (____/
|/     \|(_______)   )_(   (_______)    (_______/(_______/(_______)|/    )_)(_______/
\033[m                                          \033[35mBy: Marcus Castilho\033[m v0.1
''')
    op = int(input('''
    \033[33m[01]\033[m Complete clone
    \033[33m[02]\033[m Clone HTML
    \033[33m[03]\033[m Clone CSS
    \033[31m[04]\033[m EXIT

    └>'''))

    if op == 1:
        print('\033[31mEM DESENVOLVIMENTO...\033[m')
        sleep(2)
        clear.cls()
        continue

    elif op == 2:
        try:
            url = input('Alvo do Clone: ').lower().strip()
            codigoCorpoPage = urllib.request.urlopen(url)
            soup = BeautifulSoup(codigoCorpoPage, features="html5lib")
            titleSite = soup.title.string

            criarPage = open('index.html', 'w', encoding='utf-8')
            criarPage.write(str(soup))
            criarPage.close()

            diretorio = titleSite
            os.mkdir(diretorio)
            shutil.copy2('index.html', diretorio)
            os.remove('index.html')
            print('\033[32mSucesso!\033[m')
            sleep(1)
            print(f'Verifique o arquivo \033[33mindex.html\033[m no diretorio \033[35m{diretorio}\033[m.')
            sleep(5)
        except FileExistsError as error:
            print('Erro: {}'.format(error))
            os.remove('index.html')
            sleep(5)

    elif op == 3:
        print('\033[31mEM DESENVOLVIMENTO...\033[m')
        sleep(2)
        clear.cls()
        continue

    elif op == 4:
        clear.cls()
        break
    
    else:
        print('\033[31mOPÇÃO INVÁLIDA!\033[m')
        sleep(1)
