import sqlite3
import csv

conn = sqlite3.connect('ExempleCSV.db')
cur = conn.cursor()

resultat = cur.execute('''SELECT * FROM Població;''')

result2 = cur.fetchall()

for i,r in enumerate(resultat):
    print(f'{i}: {r}')

CSVFile = open('sortida.csv', 'w', encoding='UTF-8', newline='')
writeCSV = csv.writer(CSVFile, delimiter=',', 
                        quotechar='"', quoting=csv.QUOTE_MINIMAL) #Açò fa, si tenim: 12,5  45,6 -> "12,5","45,6"

writeCSV.writerow(['Id', 'Indicador', '1981', '1986', '1991', '1996', '2001', 
                    '2006', '2011', '2015', '2016', '2017', '2018', '2019', '2020'])

for r in resultat:
    writeCSV.writerow([r])
    