import requests
from bs4 import BeautifulSoup

url = 'https://serx.ml/search'

params = {
    'q': 'discordn.gift'
}

r = requests.get(url, params=params)


soup = BeautifulSoup(r.text, 'html.parser')

for link in soup.find_all('a', href=True):
    
    l = link['href']
    
    if l.startswith('https://'):
        
        print(l)
        #print(l.split('/')[-1])
    
    