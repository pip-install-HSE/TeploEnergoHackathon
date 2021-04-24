import csv
import xlrd


import pandas as pd

import openpyxl


data_xls = pd.read_excel('Putevye_listy.xlsx', dtype=str, engine='openpyxl', sheet_name='Документы')
data_xls.to_csv('csvfile.csv', encoding='utf-8', index=False)
1