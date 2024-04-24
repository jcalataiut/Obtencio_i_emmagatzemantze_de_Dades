from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup, element

## Aquet exemple extreu els últims 25 elements que s'han actualizat
## de la pàgina TSX. Concretament, extreu els elements que es troben
## a la secció 'Last 25 updated files'.

peticio = urllib.request.Request('https://tsx.eslamejor.com/')
peticio.add_header('User-agent','Mozilla/5.0')
html= urlopen(peticio)
htmlnet=html.read().decode()
soup=BeautifulSoup(htmlnet,'html.parser')
print(soup)

taula = soup.find('table', attrs=({'class':'head','style':'background-color:black; color:white; margin-bottom: 0.5em;'}))
files = taula.find_all('a')
for fila in files:
    print(fila.text)