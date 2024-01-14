#if there is no id then go through x path
from selenium import webdriver
#from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get('https://www.adamchoi.co.uk/overs/detailed')

button= driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
button.click()

#driver.quit()