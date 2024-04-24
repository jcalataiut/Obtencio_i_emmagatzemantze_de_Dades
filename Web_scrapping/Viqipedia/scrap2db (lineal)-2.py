# Mundial de fútbol
# https://ca.wikipedia.org/wiki/Copa_del_M%C3%B3n_de_Futbol
from urllib.request import Request, urlopen
import urllib.request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import sqlite3

url = 'https://ca.wikipedia.org/wiki/Copa_del_M%C3%B3n_de_Futbol'
htmlfile = urllib.request.urlopen(url)
soup = BeautifulSoup(htmlfile, 'html.parser')

# Pas 1 - Localitzem la taula #################################################
opcio = 1  # ← CAVIA AQUEST VALOR DEPENENT DE L'OPCIÓ QUE VULGUIS PROVAR
# Opció 1: Busquem totes les taules que apareixen en el document i ens quedem
# amb la 2a, que és la que ens interessa
# Opció 2: Busquem la taula a partir dels seus atributs:
if opcio == 1:
    taules = soup.find_all('table')
    taularesultats = taules[1]
else:
    style = 'font-size:90%; width: 100%; text-align: center;'
    taularesultats = soup.find('table',
                               attrs={'class': 'wikitable',
                                      'style': style})

# Pas 2 - Seleccionem totes les files d'aquesta taula #########################
files = taularesultats.find_all('tr')

# Pas 3 - Per cada fila, busquem tots els <td> i els processem, agafant les
# columnes que toqui ##########################################################
resultats = []
for fila in files[2:]:  # Comencem per la fila 2 (conté la info. que volem)
    dades = fila.find_all('td')  # Per cada fila, busca totes les colum.(dades)
    resultats.append({'any': dades[0].text.strip()[0:4],
                      'seu': dades[1].text.strip(),
                      'equip1': dades[2].text.strip(),
                      'equip2': dades[4].text.strip(),
                      'resultat': dades[3].text.strip()})

# Pas 4 - Mostrem els resultats per pantalla ##################################
for r in resultats:
    print(f"Any: {r['any']}, Seu: {r['seu']}, " +
          f"EQUIPS: {r['equip1']} vs {r['equip2']} " +
          f"→ RESULTAT: {r['resultat']}")

# Pas 5 - Desem els resultats a la Base de Dades ##############################
print('Connectant amb la Base de Dades...')
conn = sqlite3.connect('resultats22.db')
cur = conn.cursor()

print('Eliminant i creant la taula "Finals"...')
cur.execute('DROP TABLE IF EXISTS "Finals";')
cur.execute("""CREATE TABLE "Finals" (
    "Any"	    INTEGER PRIMARY KEY NOT NULL,
    "Seu"	    TEXT NOT NULL,
    "Equip1"	TEXT NOT NULL,
    "Equip2"	TEXT NOT NULL,
    "Resultat"	TEXT NOT NULL
    );""")
conn.commit()

print('Inserint els resultats a la taula...')
for r in resultats:
    SQL = f'''INSERT INTO Finals VALUES ({r['any']},
          "{r['seu']}","{r['equip1']}","{r['equip2']}","{r['resultat']}");'''
    cur.execute(SQL)
conn.commit()

# Fem una consulta de prova ###################################################
SQL = "SELECT * FROM Finals WHERE Seu LIKE 'A%';"
result = cur.execute(SQL)
print('Llistat dels partits jugats en una seu que comença per "A":')
for r in result:
    print(f"Any: {r[0]}, Seu: {r[1]}, " +
          f"EQUIPS: {r[2]} vs {r[3]} " +
          f"→ RESULTAT: {r[4]}")
conn.close()


