import os, csv, shutil, re
import urllib.request
from time import sleep
from bs4 import BeautifulSoup
from lib import clear, banner
#Aqui foram feitas as importações necessárias para o bom funcionamento do Programam!


while True:
    clear.cls()
    banner.nameBanner()
    try:
        op = str(input('''
\033[33m[01]\033[m Complete clone   \033[31m[Não funcional]\033[m
\033[33m[02]\033[m Clone HTML
\033[33m[03]\033[m Clone CSS        \033[31m[Não funcional]\033[m
\033[31m[04]\033[m EXIT

└> '''))
        if op == '1' or op == '01': #Essa condição será usada para fazer um clone COMPLETO de páginas web [HTML - CSS - JS]
            print('\033[31mEM DESENVOLVIMENTO...\033[m')
            sleep(2)
            clear.cls()
            continue

        elif op == '2' or op == '02': #Essa condição está configurada para clonar somente oque encontrar no HTML
            url = input('Alvo do Clone: ').lower().strip()
            nameDir01 = url.removeprefix('https://')
            url = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
            codigoCorpoPage = urllib.request.urlopen(url)
            soup = BeautifulSoup(codigoCorpoPage, features="html5lib")
            titleSite = soup.title.string
            nameDir="".join(c for c in titleSite if c.isalnum())

            criarPage = open('index.html', 'w', encoding='utf-8')
            criarPage.write(str(soup))
            criarPage.close()

            try:
                diretorio = nameDir01
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
                continue

        elif op == '3' or op == '03': #Essa condição será configurada para clonar somente oque encontrar no HTML
            print('\033[31mEM DESENVOLVIMENTO...\033[m')
            sleep(2)
            clear.cls()
            continue

        elif op == '4' or op == '04': #Essa condição está configurada para terminar o programa
            print('\033[31mVocê Escolheu sair!\033[m')
            sleep(2)
            clear.cls()
            break
        
    except ValueError:
            print('\033[31mOPÇÃO INVÁLIDA! Tente usar números\033[m')
            sleep(2)
            continue