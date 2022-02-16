import csv #Para escrever em arquivo CSV
import urllib.request #Para fazer request
from bs4 import BeautifulSoup #Função para fazer analise de dados do site

url = 'https://c4st1lh0.github.io/portifolio/index.html' #Especificando URL 
page = urllib.request.urlopen(url) #Indo ao site e armazenando o HTML na variavel
soup = BeautifulSoup(page, 'html5lib') #Fazendo parse no HTML da variavel e armazenando em formato BFS
soup.encode('utf-8') #Codificando para UTF-8


f = csv.writer(open('index.html', 'w')) #Criando o arquivo index.html com o método de escrita 'w'
f.writerow([soup]) #Escrevendo o conteúdo do site no arquivo index.html


#  ATENÇÃO!
#Essa não é a versão final! Esses são os métodos básicos e a base do projeto
