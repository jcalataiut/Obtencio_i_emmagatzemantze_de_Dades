
from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup, element
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import re
import sqlite3

### Funcions WebScrapping

def inici():
    print("Pràctica 5 - OiED 21-22")
    print("-----------------------")
    print("1 -", catnoms[0], "\n2 -", catnoms[1],
          "\n3 -", catnoms[2], "\n4 -", catnoms[3])


def quinacat():

    while True:
        cat = int(input("Quina categoria vols?"))
        if cat not in list(range(1, 5)):
            print("ERROR: Selecció no vàlida.")
        else:
            break
    return cat


def quinapag():
    while True:
        pag = input("Quina pàgina vols (1-3)? T=totes")
        if pag in ["1", "2", "3", "4"]:
            return int(pag)
        elif pag == "T":
            return pag
        else:
            print("ERROR: Selecció no vàlida.")


def proces(pag, cat):
    print("Processant pàgina", pag, "...")
    print("Categoria:", catnoms[cat-1])


def llegir_info(pag, cat):
    if pag == 1:
        fitxerhtml = urllib.request.urlopen(categories[cat-1])
    else:
        fitxerhtml = urllib.request.urlopen(
            categories[cat-1]+'?pageNo='+str(pag))

    htmlnet = fitxerhtml.read().decode()
    soup = BeautifulSoup(htmlnet, 'html.parser')
    llibres = soup.find_all('div', attrs={'class': "product-tile-container"})
    # print(len(llibres))

    titols = []
    autors = []
    preus = []
    descripcions = []
    url = []
    pagi = []
    cata = []

    for llibre in llibres:
        titol = llibre.find('h2')
        titols.append(titol.text)
        # print(titol.text)
        #autor = llibre.find('h3')

        autor = llibre.find('div', attrs={'class': "author-brand-wrapper"})
        autorT = autor.text.strip()
        autors.append(autorT)
        # print(autor.text)

        preu = llibre.find('span', attrs={'class': 'sales'})
        preuT = float(preu.text.strip().replace(",",".").replace("€",""))
        preus.append(preuT)

        descripcio = llibre.find('div', attrs={'class': 'product-desc'})
        descripcioT = descripcio.text.strip()
        descripcions.append(descripcioT)

        if pag == 1:
            url.append(categories[cat-1])
        else:
            url.append(categories[cat-1]+'?pageNo='+str(pag))

        cata.append(cat)

        pagi.append(int(pag))

    return {"titols": titols, "autors": autors, "preus": preus, "descripcions": descripcions, "url": url, "pagi": pagi, "cata": cata}


def printar(dic):
    for i in range(len(dic["titols"])):
        print(f'Pàgina {dic["pagi"][i]}: "{dic["titols"][i]}" ({dic["autors"][i]}) - Preu: {dic["preus"][i]}€ - Descripció:"{dic["descripcions"][i][0:15]}..."', end="\n")

def basedades():
    conn = sqlite3.connect('llibres.db')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS "Llibres";')
    conn.commit()

    # TAULA LLIBRES
    cur.execute("""CREATE TABLE "Llibres" (
        "Clau"         INTEGER PRIMARY KEY NOT NULL,
        "Titol"        TEXT,
        "Autor"        TEXT,
        "Preu"         FLOAT,
        "Descripcio"   TEXT,
        "URL"          TEXT NOT NULL,
        "Pagina"       INTEGER NOT NULL,
        "Categoria"    INTEGER NOT NULL
        );""")
    conn.commit()

    # TAULA CATEGORIES
    cur.execute('DROP TABLE IF EXISTS "CATEGORIES";')
    conn.commit()

    cur.execute("""CREATE TABLE CATEGORIES (
        "Id"        INTEGER PRIMARY KEY
                    NOT NULL
                    REFERENCES "Llibres" ("Categoria"),
        "Categoria" TEXT NOT NULL
    );""")
    conn.commit()

    for i in range(len(catnoms)):
        SQL2=f'''INSERT INTO "CATEGORIES" VALUES ({i+1},"{catnoms[i]}");'''
        cur.execute(SQL2)
        conn.commit()
    
    conn.close()

def insertar(dic, cont):
    conn = sqlite3.connect('llibres.db')
    cur = conn.cursor()
    acum=cont
    for i in range(len(dic["pagi"])):
        SQL=f"""INSERT INTO "Llibres" VALUES ({cont+i+1}, "{dic["titols"][i]}", "{dic["autors"][i]}", 
                {dic["preus"][i]}, "{dic["descripcions"][i]}", "{dic["url"][i]}", {dic["pagi"][i]}, {dic["cata"][i]});"""
        
        cur.execute(SQL)
        conn.commit()
        acum=cont+i+1

    return acum

def consultes():
    print("-------")
    print("CONSULTES")
    print("--------\n")

    conn = sqlite3.connect('llibres.db')
    cur = conn.cursor()

    print("Consulta 1. - Quin és el preu mitjà dels llibres presentats?")
    SQL = f"""SELECT AVG("Preu") FROM "Llibres";"""
    resultat=cur.execute(SQL)
    for r in resultat:
        print(f"Preu mitjà: {round(r[0],2)}€")
    
    print("\nConsulta 2. - Quin és el llibre més car dels seleccionats?")
    SQL2=f"""SELECT "Clau","Titol","Autor","Preu"
             FROM "Llibres"
             WHERE "Preu">=(SELECT MAX("Preu") FROM "Llibres");"""
    resultat2=cur.execute(SQL2)
    
    for r in resultat2:
        print(f"""El llibre més car és "{r[1]}" ({r[2]}) - {r[3]}€   (Id: {r[0]})""")

    print("\nConsulta 3. - Quin és el llibre més econòmic dels seleccionats?")
    SQL3=f"""SELECT "Clau","Titol","Autor","Preu"
             FROM "Llibres"
             WHERE "Preu"<=(SELECT MIN("Preu") FROM "Llibres");"""
    resultat3=cur.execute(SQL3)
    
    for r in resultat3:
        print(f"""El llibre més econòmic és "{r[1]}" ({r[2]}) - {r[3]}€   (Id: {r[0]})""")


        
def main():
    inici()
    basedades()
    cat = quinacat()
    pag = quinapag()
    proces(pag, cat)
    if pag == "T":
        cont=-1
        for i in range(1, 4):
            dic = llegir_info(i, cat)
            printar(dic)
            cont=insertar(dic,cont)
    else:
        dic = llegir_info(pag, cat)
        printar(dic)
        insertar(dic,-1)
    consultes()


# PROGRAMA PRINCIPAL

# CATEGORIES
cat1 = 'https://www.abacus.coop/ca/llibres/art-cinema-i-musica'
cat2 = 'https://www.abacus.coop/ca/llibres/ciencia-i-coneixement'
cat3 = 'https://www.abacus.coop/ca/llibres/comic'
cat4 = 'https://www.abacus.coop/ca/llibres/guies-de-viatge'

categories = [cat1, cat2, cat3, cat4]
catnoms = ["Art, cinema i música",
           "Ciència i coneixement", "Còmic", "Guies de viatge"]


main()

