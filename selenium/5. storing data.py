from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get('https://www.adamchoi.co.uk/overs/detailed')

button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
button.click()

matches= driver.find_elements(By.TAG_NAME,'tr' )

date=[]
home_team=[]
score=[]
away_team=[]

for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home= (match.find_element(By.XPATH,'./td[2]').text)
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH,'./td[3]').text)
    away_team.append(match.find_element(By.XPATH,'./td[4]').text)
driver.quit()

df= pd.DataFrame({'date':date,'home_team':home_team,'score':score, 'away_team':away_team })
df.to_csv('football_data.csv', index=False)

print(df)