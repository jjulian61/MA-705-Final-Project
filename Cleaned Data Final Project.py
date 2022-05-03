# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:42:01 2022

@author: jjuli
"""


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
import pickle

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

service=Service("C://Users//jjuli//Desktop//chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.zillow.com/new-york-ny/condos/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.95826505568351%2C%22east%22%3A-72.59345792677726%2C%22south%22%3A40.07489137772138%2C%22north%22%3A41.031342810545354%7D%2C%22mapZoom%22%3A9%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22priced%22%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D")
time.sleep(2)
x=driver.find_element(By.XPATH, "//h1[@class='search-title']")
x.click()

actions = ActionChains(driver)
for _ in range(300):
    actions.send_keys(Keys.ARROW_DOWN).perform()

propTypes=driver.find_elements(By.XPATH,"//li[@class='list-card-statusText']")
prices=driver.find_elements(By.XPATH,"//div[@class='list-card-price']")
listers=driver.find_elements(By.XPATH,"//p[@class='list-card-extra-info']")
addresses=driver.find_elements(By.XPATH,"//address[@class='list-card-addr']")
beds=driver.find_elements(By.XPATH, "//ul[@class='list-card-details']/li[@class=''][1]")
baths=driver.find_elements(By.XPATH, "//ul[@class='list-card-details']/li[@class=''][2]")
sqFts=driver.find_elements(By.XPATH, "//ul[@class='list-card-details']/li[@class=''][3]")

propTypesList=[]
pricesList=[]
listersList=[]
addressesList=[]
bedsList=[]
bathsList=[]
sqFtsList=[]

i=0
for x in propTypes:
    propTypesList.insert(i, cleanhtml(x.get_attribute("innerHTML")))
    i+=1
i=0
for x in prices:
    pricesList.insert(i, cleanhtml(x.get_attribute("innerHTML")))
    i+=1
i=0
for x in listers:
    tempString=cleanhtml(x.get_attribute("innerHTML"))
    tempString=tempString[tempString.find("LISTING BY: ")+12:tempString.find("LISTING BY: ")+112]
    tempString=tempString[0:tempString.find(" (")]
    listersList.insert(i, tempString)
    i+=1
i=0
for x in addresses:
    addressesList.insert(i, cleanhtml(x.get_attribute("innerHTML")))
    i+=1
i=0
for x in beds:
    bedsList.insert(i, cleanhtml(x.get_attribute("innerHTML")))
    i+=1
i=0
for x in baths:
    bathsList.insert(i, cleanhtml(x.get_attribute("innerHTML")))
    i+=1
i=0
for x in sqFts:
    sqFtsList.insert(i, cleanhtml(x.get_attribute("innerHTML")))
    i+=1

print(propTypesList)
print(pricesList)
print(listersList)
print(addressesList)
print(bedsList)
print(bathsList)
print(sqFtsList)

dictionary = {"Property Types":propTypesList, "Prices":pricesList, "Listers":listersList, "Addresses":addressesList, "Beds":bedsList, "Baths":bathsList, "Sq. Ft.":sqFtsList}
pickle.dump(dictionary, open('PropertyListings.pkl', 'wb'))
object = pd.read_pickle(r'PropertyListings.pkl')
