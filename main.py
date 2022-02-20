from lib import clear, banner, cloneSite
from time import sleep
import os

#Aqui foram feitas as importações necessárias para o bom funcionamento do Programam!

while True:
    clear.cls()
    banner.nameBanner()
    try:
        op = str(input('''
\033[33m[01]\033[m Clone code Site      \033[33mBETA\033[m
\033[33m[02]\033[m Decompilar APK       \033[33mEM DEV\033[m
\033[31m[03]\033[m EXIT

└> '''))
    except ValueError:
            print('\033[31mOPÇÃO INVÁLIDA! Tente usar números\033[m')
            sleep(2)
            continue

    if op == '1' or op == '01': 
        cloneSite.clone()
        #Essa condição está configurada para clonar somente oque encontrar no HTML

    elif op == '2' or op =='02':
        path = input('Caminho do arquivo: ')
        dir = os.path.abspath(path)
        print(dir)
        sleep(10)
        
    elif op == '3' or op == '03': #Essa condição está configurada para terminar o programa
        print('\033[31mVocê Escolheu sair!\033[m')
        sleep(2)
        clear.cls()
        break