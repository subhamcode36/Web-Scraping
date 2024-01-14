from selenium import webdriver

website= 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/91773/Downloads/chrome driver'
driver = webdriver.Chrome(path)
driver.get(website)