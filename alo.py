import os

from dotenv import load_dotenv
import matplotlib.pyplot as plt
from pandas.plotting import table  # EDIT: see deprecation warnings below

from PIL import Image

load_dotenv()
from peewee import *
import pandas as pd
import math
import datetime

db = PostgresqlDatabase(
    database=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USERNAME"),
    password=os.environ.get("DB_PASSWORD"),
    host=os.environ.get("DB_HOST"),
    port=os.environ.get("DB_PORT")
)



def getEff(x, y):
    if y == 0:
        return -1
    if x > y:
        return 1
    return x / y



def getMidEff(x, y):
    if y == 0:
        return "-"
    if x > y:
        return 1
    return round(x / y, 2)



def getPngCustomer():
    data = pd.read_csv('dynamic.csv', delimiter=',',
                       names=['vehicle_index', 'date', 'predict_time', 'real_time', 'customer', 'vehicle'])
    data['efficiency'] = data.apply(lambda x: getEff(x['real_time'], x['predict_time']), axis=1)
    customers = data['customer'].unique()
    vehicles = data['vehicle'].unique()

    counts = {customer: [0, 0] for customer in customers}
    # counts = {[0]}* len(customers)
    for note in data.values:
        if counts[note[4]][1] != -1:
            print(counts[note[4]][1])
            counts[note[4]][0] += 1
            counts[note[4]][1] += note[6]

    eff = [round(counts[c][1] / counts[c][0], 2) for c in customers]
    customer_data = pd.DataFrame()
    customer_data['Заказчик'] = customers
    customer_data['Эффективность'] = eff
    customer_data['Среднее время простоя от выделенного, %'] = [round((1 - counts[c][1] / counts[c][0]) * 100, 2) for c
                                                                in customers]
    customer_data['Число выполненных заявок'] = [counts[c][0] for c in customers]
    # sns.heatmap(customer_data[:, 1:], annot=True, fmt='.1g')
    plt.figure(figsize=(30, 30))
    ax = plt.subplot(111, frame_on=False)  # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    table(ax, customer_data, rowLabels=[''] * customer_data.shape[0], loc='center')

    plt.savefig('dynamic.jpg')

def getPngTransport():
    data = pd.read_csv('dynamic.csv', delimiter=',',
                       names=['vehicle_index', 'date', 'predict_time', 'real_time', 'customer', 'vehicle'])
    data['efficiency'] = data.apply(lambda x: getEff(x['real_time'], x['predict_time']), axis=1)
    customers = data['customer'].unique()
    vehicles = data['vehicle'].unique()
    # copydata = data.copy()
    # copydata.drop(columns=['vehicle_index', 'date', 'predict_time', 'real_time', 'vehicle'])
    counts = {customer: {v: [0, 0] for v in vehicles} for customer in customers}
    for note in data.values:
        if counts[note[4]][note[5]][1] != -1:
            print(counts[note[4]][note[5]][1])
            counts[note[4]][note[5]][0] += 1
            counts[note[4]][note[5]][1] += note[6]
    eff = [[getMidEff(counts[c][v][1], counts[c][v][0]) for v in counts[c]] for c in customers]
    customer_data = pd.DataFrame()
    customer_data["ТС"] = vehicles
    for i, c in enumerate(customers):
        customer_data[c] = eff[i]

    plt.figure(figsize=(60, 60))
    ax = plt.subplot(111, frame_on=False)  # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    table(ax, customer_data, rowLabels=[''] * customer_data.shape[0], loc='center')
    # table(ax, customer_data)  # where df is your data frame

    plt.savefig('dynamic2.jpg')





getPngTransport()
getPngCustomer()
