import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path='C:/Users/minahil/Desktop/chromedriver.exe')
driver.get('https://www.techradar.com/')
results = []
news = []
list1 = []
x = []
y = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

for a in soup.find_all(attrs='sc-bczRLJ ftDECR'):
    name = a.find('ul')
    if name not in results:
        results.append(name.text)

for b in soup.find_all(attrs='content'):
    data = b.find('h3')
    if data not in news:
        news.append(data.text)

for c in soup.find_all(attrs='popular-box__articles-list'):
    row = c.find('li')
    if row not in list1:
        list1.append(row.text)

for d in soup.find_all(attrs='byline'):
    author = d.find('span')
    if author not in x:
        x.append(author.text)

for e in soup.find_all(attrs='locale-links__item'):
    regions = e.find('a')
    if regions not in y:
        y.append(regions.text)

df = pd.DataFrame({'Names':results})
df.to_csv('Names.csv', index=False, encoding='utf-8')

df = pd.DataFrame({'Latest News':news})
df.to_csv('data.csv', index=False, encoding='utf-8')

df = pd.DataFrame({'Author':x})
df.to_csv('author.csv', index=False, encoding='utf-8')

df = pd.DataFrame({'Regions':y})
df.to_csv('regions.csv', index=False, encoding='utf-8')

df = pd.DataFrame({'Most Popular':list1})
df.to_csv('popular.csv', index=False, encoding='utf-8')