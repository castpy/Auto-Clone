import os #Chamando funçoes do sistema
import csv #Para escrever em arquivo CSV
import shutil #Para copiar arquivos
import urllib.request #Para fazer request
from time import sleep #Para fazer uma contagem em segundos
from bs4 import BeautifulSoup #Função para fazer analise de dados do site

url = 'https://www.facebook.com/' #Especificando URL 
page = urllib.request.urlopen(url) #Indo ao site e armazenando o HTML na variavel
soup = BeautifulSoup(page, 'html5lib') #Fazendo parse no HTML da variavel e armazenando em formato BFS
tituloSite = soup.title.string #Buscando TITULO do site
soup.encode('utf-8') #Codificando para UTF-8


f = csv.writer(open('index.html', 'w', encoding='UTF-8')) #Criando o arquivo index.html com o método de escrita 'w'
f.writerow([soup]) #Escrevendo o conteúdo do site no arquivo index.html


dir = tituloSite #Adicionando titulo do site como nome do diretório
os.mkdir(dir) #Criando o diretório com o titulo do site

sleep(1)
shutil.move('index.html', dir) #Movendo arquivo para o diretório

#  ATENÇÃO!
#Essa não é a versão final! Esses são os métodos básicos e a base do projeto
