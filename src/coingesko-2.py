from bs4 import BeautifulSoup as soup
from selenium import webdriver

url='https://coinmarketcap.com/currencies/bitcoin/news/'

driver = webdriver.Safari()
driver.get(url)

page = driver.page_source
page_soup = soup(page,'html.parser')

containers = page_soup.findAll("div",{"class":"product"})
print(containers)
print(len(containers))