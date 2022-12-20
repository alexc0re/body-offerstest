import pandas as pd
import requests
from io import StringIO


url = 'https://docs.google.com/spreadsheets/d/1OWQFG-IeLMy7oVV27C41Tb0Z1ATXamO0fYu38_Wiq-o/gviz/tq?tqx=out:csv&' \
          'sheet=test' # сюда прописываем название таблицы

sheet_name = url.split('/')[-1]  # gets sheet name for dl link
print()
print(sheet_name)
file_id = url.split('/')[-3]  # gets file ID from google sheets
print()
print(file_id)
dwn_url = 'https://docs.google.com/spreadsheets/d/' + file_id + '/gviz/' + sheet_name
url2 = requests.get(dwn_url).text
csv_raw = StringIO(url2)
linksDF = pd.read_csv(csv_raw)
print(linksDF)
