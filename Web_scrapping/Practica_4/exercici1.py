from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup, element
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import re 

fitxerhtml=urllib.request.urlopen('http://infomet.meteo.ub.edu/clima/consulta/')
htmldecodificat=fitxerhtml.read().decode('cp1252')
htmlnet = htmldecodificat.replace('\r', '').replace('\n', '').replace('\t', '')
#print(htmlnet)
resultats = re.findall(r'TARGET="blank">(.*?)<', htmlnet)
lista=[]
cont=0
for resultat in resultats:
    cont+=1
    resultat=resultat.strip()
    if resultat in lista:
        pass
    else: 
        lista.append(resultat)

print("Total",cont,"ciutats trobades")
print("Eliminant repeticions queden",len(lista),"ciutats")
for i in range(len(lista)):
    print("Ciutat",i+1,"=",lista[i])

 


#peticio = urllib.request.Request('https://www.tdt1.com/canales-barcelona/')
#peticio.add_header('User-agent','Mozilla/5.0')  # Per poder "enganyar" el servidor
#html = urlopen(peticio)
#htmlnet = html.read().decode('iso-8859-15')

#soup = BeautifulSoup(htmlnet,'html.parser')
#numtaula=1
#taules = soup.find_all('table', attrs={'border':'0', 'width':'100%'})
#for taula in taules:
#    files = taula.find_all('tr')
#    numfiles = len(files)
#    if numtaula == 1 :
#        desde = 1
#    else:
#        desde =0
#    for i in range(desde,numfiles):
#        fila = files[i]
#        elements = fila.find_all('td')
#        print(f'Taula {numtaula} - fila {i}: {elements[1].text.strip()}, EPG: {elements[3].text.strip()}')
#    numtaula = numtaula + 1



