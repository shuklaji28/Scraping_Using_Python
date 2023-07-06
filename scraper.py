# import requests
# import csv
# from bs4 import BeautifulSoup

# url="https://www.linkedin.com/feed/"
# r=requests.get(url)
# # print(r.content)

# soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())
import csv
import requests 
from bs4 import BeautifulSoup
import html5lib

url="http://www.values.com/inspirational-quotes"
r=requests.get(url)
soup=BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())
quotes=[]
table=soup.find('div', attrs={'id':'all_quotes'})

for row in table.findAll('div',
                         attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
   
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in  quotes:
        w.writerow(quote)