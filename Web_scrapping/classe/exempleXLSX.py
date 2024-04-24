import sqlite3
import xlsxwriter

conn = sqlite3.connect('ExempleCSV.db')
cur = conn.cursor()

resultat = cur.execute('''SELECT * FROM Població;''')

result2 = cur.fetchall()

for i,r in enumerate(resultat):
    print(f'{i}: {r}')


headers = ['Id', 'Indicador', '1981', '1986', '1991', '1996', '2001', 
                    '2006', '2011', '2015', '2016', '2017', '2018', '2019', '2020']

workbook = xlsxwriter.Workbook('sortida.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column_format(0,0,21) #set_column_format(col_inicial, col_final, Pixels)
worksheet.set_column_format(1,1,230)
worksheet.set_column_format(2,14, 50)

head_format = workbook.add_format({'bold':True, 'bg_color':'#5B9B'})
strip1_format = workbook.add_format({'bold':False, 'bg_color':'DDEBF7'})
strip2_format = workbook.add_format({'bold':False, 'bg_color':'FFFFFF'})


for i,head in enumerate(headers):
    worksheet.write(0, i, head, head_format) # write(fila, columna, item, format)
### El format de la cel·la pot ser: date_format, money_format...

fila=1
for l in resultat:
    for i in range(0,len(l)):
        if fila%2 == 0: # Di és una línia parell, fara servir el format
            format_strip = strip1_format
        else:
            format_strip = strip2_format
        worksheet.write(fila, i, res[i])
    fila+=1