import os, csv, shutil
import urllib.request
from bs4 import BeautifulSoup

#url = input('Alvo do Clone: ').lower().strip()
url = 'https://c4st1lh0.github.io/portifolio/'
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

