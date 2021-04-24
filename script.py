import csv
import xlrd

import pandas as pd

import openpyxl

#
# data_xls = pd.read_excel('Putevye_listy.xlsx', dtype=str, engine='openpyxl', sheet_name='Документы')
# data_xls.to_csv('csvfile.csv', encoding='utf-8', index=False)


from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:fnvjYUbf63nv@193.162.143.45:5432/postgres", echo=False)
df = pd.read_csv("csvfile.csv")
df.to_sql("schema.table", con=engine)
