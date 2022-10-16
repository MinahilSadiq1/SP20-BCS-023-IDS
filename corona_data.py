import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path='C:/Users/minahil/Desktop/chromedriver.exe')
driver.get('https://docs.google.com/spreadsheets/d/1nHZopMQpvDO1ETpMVP6ZJ22wk3fHRgB00sekIvqXB_c/pubhtml?gid=1648546042#')

results = []


content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

for a in soup.find_all(attrs='row-headers-background'):
    name = a.find('tr')
    if name not in results:
        results.append(name.text)

df = pd.DataFrame({'Latest data':results})
df.to_csv('data.csv', index=False, encoding='utf-8')
