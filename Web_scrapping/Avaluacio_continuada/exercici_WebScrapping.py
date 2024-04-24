from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup, element
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import re 

print("Exercici WebScrapping - OiED 21-22")
print("----------------------------------")

peticio = urllib.request.Request('https://www.km77.com/coches/citroen/c3/2017/estandar/informacion')
peticio.add_header('User-agent','Mozilla/5.0')
html= urlopen(peticio)
htmlnet=html.read().decode()
soup=BeautifulSoup(htmlnet,'html.parser')
#print(soup)

taula = soup.find('div', attrs={'class':'module-container d-lg-block'})
files = taula.find_all('tr')
for i in range(2,9):
    info=files[i].find('td')
    print(info.text.strip())
