import mysql.connector
import pandas as pd
from pandas import DataFrame
import psycopg2 as psy
conn = mysql.connector.connect(
    user='root', 
    password='Pavanms@1234', 
    host='127.0.0.1', 
    database='scrapp',
    port='3306'
    )

cursor = conn.cursor()
print("database connected")

sql = '''SELECT * from scrapping where Year>=2021'''

cursor.execute(sql)
result = cursor.fetchall();
print(result)
# df=pd.read_sql(sql,conn)
# print(df)

conn.close()
