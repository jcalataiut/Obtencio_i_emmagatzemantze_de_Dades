from urllib.request import Request, urlopen
import urllib
from bs4 import BeautifulSoup, element

peticio = urllib.request.Request('http://davidarbona.com/')
peticio.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
html= urlopen(peticio)
htmlnet=html.read().decode()
soup=BeautifulSoup(htmlnet,'html.parser')

taulacol = soup.find('div', attrs=({'class':"wp-block-cover has-background-dim serveis",'style':"background-color:#eaccc2"}))
taulesprin = taulacol.find_all('div', attrs=({'class':"wp-block-columns"}))
print(taulesprin[1])
print('------------')
for t1 in taulesprin:
    taulescol = t1.find_all('div', attrs=({'class':"wp-block-column"}) )
    for t2 in taulescol:
        if len(t2)!=0:
            # Primer trobem el titul
            titul = t2.find('h4', attrs=({'class':"has-text-align-center"}))
            titul_mes = titul.find('a')
            print(titul_mes.text)
            print('----------------------')
            #Ara fem els paragrafs
            par = t2.find_all('p',attrs=({'class':"has-text-color has-text-align-center has-very-dark-gray-color"}))
            for p in par:
                print(p.text)
            print('/n')
    