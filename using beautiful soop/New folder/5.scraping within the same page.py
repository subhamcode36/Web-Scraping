from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies'
response = requests.get(website)
content = response.text
soup = BeautifulSoup(content, "lxml")
#print(soup.prettify()) 

box = soup.find('article', class_='main-article')

links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

print(links)

for link in links:
    website = f'{root}/{link}'
    response = requests.get(website)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    
    box = soup.find('article', class_='main-article')
  
    title = box.find('h1').get_text() #<h1>Titanic (1997) - full transcript</h1>
    transcript = box.find('div',class_="full-script").get_text(strip=True, separator='')

    with open(f'{title}.txt','w') as file: #title + txt
     file.write(transcript)
