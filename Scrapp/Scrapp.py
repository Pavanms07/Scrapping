import csv
import pandas as pd
import numpy as np
import openpyxl,requests
from bs4 import BeautifulSoup
import os
import xlsxwriter

from datetime import date


url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text)
tr = soup.findChildren("tr")
tr = iter(tr)
next(tr)



new_list = []
for movie in tr:
        title = movie.find('td', {'class': 'titleColumn'} ).find('a').contents[0]
        year = movie.find('td', {'class': 'titleColumn'} ).find('span', {'class': 'secondaryInfo'}).contents[0]
        rating = movie.find('td', {'class': 'ratingColumn imdbRating'} ).find('strong').contents[0]
        today = date.today()
        row = [title,year,rating,today]
        if row  not in new_list:
            new_list.append(row)
print(len(new_list))
index_labels=range(1,len(new_list)+1)
Scrapp_data = pd.DataFrame(new_list, columns=['Movie','Year','Rating','Data of Date'],index=index_labels)
Scrapp_data['Year']=Scrapp_data['Year'].str.replace('(', ' ', regex=True)
Scrapp_data['Year']=Scrapp_data['Year'].str.replace(')', ' ', regex=True)
Scrapp_data.index.names = ['ID']

print(Scrapp_data)
Scrapp_data.to_csv("Scrapped_datacsv.csv")

Scrapp_data.to_excel("Scrapped_dataexcel.xlsx")
Scrapp_data.to_json("Scrapped_datajson.json")

print("Total received data :" ,len(Scrapp_data)," records on  ",    today)
print("\nSucceed")
