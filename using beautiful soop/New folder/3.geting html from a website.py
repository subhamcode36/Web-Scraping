from bs4 import BeautifulSoup
import requests
website = "https://subslikescript.com/movie/Titanic-120338"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
#print(soup.prettify()) 

box = soup.find('article', class_='main article') 
#print(box)
title = soup.find('h1').get_text() #<h1>Titanic (1997) - full transcript</h1>
#print(title)
transcript = soup.find('div',class_="full-script").get_text(strip=True, separator='')
print(title)
print(transcript)







