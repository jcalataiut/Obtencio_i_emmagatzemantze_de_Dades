from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup, element
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import re 

print("Pràctica 4 - Exercici 2 --------------------")
fitxerhtml=urllib.request.urlopen('https://www.uab.cat/web/agenda-1345828727305.html')
htmldecodificat=fitxerhtml.read().decode('utf-8')
htmlnet = htmldecodificat.replace('\r', '').replace('\n', '').replace('\t', '')
#print(htmlnet)

resultTEXT = re.findall(r'<h3><a href=.*?>(.*?)</a>            </h3>', htmlnet)
resultDATA = re.findall(r'<li class="data">(.*?)</li>', htmlnet)
for i in range(len(resultTEXT)):
    print(resultDATA[i], end=":")
    print( resultTEXT[i])

