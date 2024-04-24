
from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup, element
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import re 

def inici():
    print("Pràctica 5 - OiED 21-22")
    print("-----------------------")
    print("1 -", catnoms[0], "\n2 -", catnoms[1], "\n3 -", catnoms[2], "\n4 -", catnoms[3])

def quinacat():

    while True: 
        cat=int(input("Quina categoria vols?"))
        if cat not in list(range(1,5)):
            print("ERROR: Selecció no vàlida.")
        else:
            break
    return cat

def quinapag():
    while True:
        pag = input("Quina pàgina vols (1-3)? T=totes")
        if pag in ["1","2","3","4"]:
            return int(pag)
        elif pag=="T":
            return pag
        else:
            print("ERROR: Selecció no vàlida.")

def proces(pag, cat):
    print("Processant pàgina",pag,"...")
    print("Categoria:",catnoms[cat-1])


def llegir_info(pag, cat):
    if pag==1:
        fitxerhtml=urllib.request.urlopen(categories[cat-1])
    else:
        fitxerhtml=urllib.request.urlopen(categories[cat-1]+'?pageNo='+str(pag))

    htmlnet=fitxerhtml.read().decode()
    soup = BeautifulSoup(htmlnet,'html.parser')
    llibres = soup.find_all('div', attrs={'class':"product-tile-container"})
    #print(len(llibres))

    titols=[]
    autors=[]
    preus=[]
    descripcions=[]

    for llibre in llibres:
        titol = llibre.find('h2')
        titols.append(titol.text)
        #print(titol.text)
        #autor = llibre.find('h3')

        autor = llibre.find('div',attrs={'class':"author-brand-wrapper"})
        autorT = autor.text.strip()
        autors.append(autorT)
        #print(autor.text)

        preu = llibre.find('span', attrs={'class':'sales'})
        preuT=preu.text.strip()
        preus.append(preuT)

        descripcio = llibre.find('div', attrs={'class':'product-desc'})
        descripcioT = descripcio.text.strip()
        descripcions.append(descripcioT)
    
    return {"titols":titols, "autors":autors, "preus":preus, "descripcions":descripcions}

def printar(dic, pag):
    for i in range(len(dic["titols"])):
        print(f'Pàgina {pag}: "{dic["titols"][i]}" ({dic["autors"][i]}) - Preu: {dic["preus"][i]} - Descripció:"{dic["descripcions"][i][0:15]}..."', end="\n")


def main():
    inici()
    cat=quinacat()
    pag=quinapag()
    proces(pag, cat)
    if pag=="T":
        for i in range(1,4):
            dic=llegir_info(i,cat)
            printar(dic, i)
    else:
        dic=llegir_info(pag,cat)
        printar(dic, pag)


### PROGRAMA PRINCIPAL

#CATEGORIES
cat1 = 'https://www.abacus.coop/ca/llibres/art-cinema-i-musica'
cat2 = 'https://www.abacus.coop/ca/llibres/ciencia-i-coneixement'
cat3 = 'https://www.abacus.coop/ca/llibres/comic'
cat4 = 'https://www.abacus.coop/ca/llibres/guies-de-viatge'

categories=[cat1,cat2,cat3,cat4]
catnoms=["Art, cinema i música","Ciència i coneixement","Còmic","Guies de viatge"]

main()












#print("Pràctica 5 - OiED 21-22")
#print("-----------------------")

#CATEGORIES
#cat1 = 'https://www.abacus.coop/ca/llibres/art-cinema-i-musica'
#cat2 = 'https://www.abacus.coop/ca/llibres/ciencia-i-coneixement'
#cat3 = 'https://www.abacus.coop/ca/llibres/comic'
#cat4 = 'https://www.abacus.coop/ca/llibres/guies-de-viatge'

#categories=[cat1,cat2,cat3,cat4]
#catnoms=["Art, cinema i música","Ciència i coneixement","Còmic","Guies de viatge"]

#print("1 -", catnoms[0], "\n2 -", catnoms[1], "\n3 -", catnoms[2], "\n4 -", catnoms[3])

#while True:
#    cat=int(input("Quina categoria vols?"))
#    if cat not in list(range(1,5)):
#        print("ERROR: Selecció no vàlida.")
#    else:
#        break

#while True:
#    pag = int(input("Quina pàgina vols (1-3)?"))
#    if pag not in list(range(1,4)):
#        print("ERROR: Selecció no vàlida.")
#    else:
#        break

#print("Processant pàgina",pag,"...")
#print("Categoria:",catnoms[cat-1])

#if pag==1:
#    fitxerhtml=urllib.request.urlopen(categories[cat-1])
#else:
#    fitxerhtml=urllib.request.urlopen(categories[cat-1]+'?pageNo='+str(pag))

#htmlnet=fitxerhtml.read().decode()
#soup = BeautifulSoup(htmlnet,'html.parser')
#llibres = soup.find_all('div', attrs={'class':"product-tile-container"})
#print(len(llibres))

#for llibre in llibres:
#    titol = llibre.find('h2')
    #print(titol.text)
    #autor = llibre.find('h3')
#    autor = llibre.find('div',attrs={'class':"author-brand-wrapper"})
#    autorT = autor.text.strip()
    #print(autor.text)
#    preu = llibre.find('span', attrs={'class':'sales'})
#    preuT=preu.text.strip()
#    descripcio = llibre.find('div', attrs={'class':'product-desc'})
#    descripcioT = descripcio.text.strip()
#    print(f'Pàgina {pag}: "{titol.text}" ({autorT}) - Preu: {preuT} - Descripció:"{descripcioT[0:15]}..."', end="\n")


