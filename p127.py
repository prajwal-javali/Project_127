from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv



url =  'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(url,verify=False)

soup = BeautifulSoup(page.text , "html.parser")

star_table = soup.find("table")

templist = []

tablerows = star_table.find_all("tr")

for tr in tablerows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    templist.append(row) 


Star_names = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(templist)):
    Star_names.append(templist[i][1])
    Distance.append(templist[i][3])
    Mass.append(templist[i][5])
    Radius.append(templist[i][6])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])

df2.to_csv('star.csv')















