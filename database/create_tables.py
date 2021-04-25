import os
from dotenv import load_dotenv
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


class BaseModel(Model):
    class Meta:
        database = db

class Customer(BaseModel):
    name = CharField(null=False, unique=True)

class Vehicle(BaseModel):
    name = CharField(null=False, unique=True)

class License(BaseModel):
    name = CharField(null=False, unique=True, max_length=16)

# class Service(BaseModel):
#     name = CharField(unique=True)

class Order(BaseModel):
    customer = ForeignKeyField(Customer, null=False, backref='orders')
    vehicle = ForeignKeyField(Vehicle, null=False, backref='orders')
    license = ForeignKeyField(License, null=True, backref='orders')
    minutes = IntegerField(null=False)
    date = CharField(null=False, max_length=16)
    is_completed = BooleanField(null=False)

class Event(BaseModel):
    name = CharField(null=False, unique=True, max_length=64)

class Ride(BaseModel):
    event = ForeignKeyField(Event, null=False, backref='rides')
    license = ForeignKeyField(License, null=True, backref='rides')
    date = CharField(null=False, max_length=16)
# class Order(BaseModel):
#     numb

# class Tweet(BaseModel):
#     user = ForeignKeyField(User, backref='tweets')
#     message = TextField()
#     created_date = DateTimeField(default=datetime.datetime.now)
#     is_published = BooleanField(default=True)
if __name__ == '__main__':
    db.connect(reuse_if_open=True)
    tables = [Order, Ride, Customer, Vehicle, License, Event]
    for table in tables:
        try:
            db.drop_tables([table])
        except:
            print(f'Can not delete {table}')
    db.create_tables(tables)

    orders_data_frame = pd.read_excel(io='./orders_small.xlsx', sheet_name='Документы')

    for el in orders_data_frame['Заказчик']:
        if not Customer.select().where(Customer.name == el):
            Customer.insert(name=el).execute()

    for el in orders_data_frame['Требование_кТС']:
        if not Vehicle.select().where(Vehicle.name == el):
            Vehicle.insert(name=el).execute()

    for el in orders_data_frame['НазначеноТС']:
        if isinstance(el, float) and math.isnan(el):
            continue
        if not License.select().where(License.name == el):
            License.insert(name=el).execute()

    for i, row in orders_data_frame.iterrows():
        # if i > 5:
        #     break

        is_completed = True if 'исполнен' in row['СтатусЗаявки'].lower() else False
        start_time = row['ВремяРаботС']
        end_time = row['ВремяРаботПо']
        if not is_completed:
            delta_time = 0
        else:
            if (isinstance(start_time, float) and math.isnan(start_time)) or \
                        (isinstance(end_time, float) and math.isnan(end_time)):
                continue
            else:
                delta_time = int(end_time[0:2]) * 60 + \
                             int(end_time[3:5]) - \
                             int(start_time[0:2]) * 60 - \
                             int(start_time[3:5])
                if delta_time == 0:
                    delta_time = 24 * 60 * 60

        # if math.isnan(start_time) or math.isnan(end_time):
        #     continue
        # if not row['ВремяРаботС'] or not row['ВремяРаботПо'] \
        #         or row['ВремяРаботС'] == 'nan' or row['ВремяРаботПо'] == 'nan':
        #     continue

        # print(f'"{start_time}" - "{end_time}"')
        # print(delta_time)
        Order.insert(
            customer=Customer.select().where(Customer.name == row['Заказчик']),
            vehicle=Vehicle.select().where(Vehicle.name == row['Требование_кТС']),
            license=License.select().where(License.name == row['НазначеноТС']),
            minutes=delta_time,
            date=row['ДатаВыполненияС'][:10],
            is_completed=is_completed
        ).execute()
        # print(start_time)
        # print(end_time)
        # print()

        rides_data_frame = pd.read_excel(io='./rides_small.xlsx', sheet_name='Поездки по данным GPS')

        for el in rides_data_frame['Событие']:
            if not Event.select().where(Event.name == el):
                Event.insert(name=el).execute()

        for i, row in rides_data_frame.iterrows():
            # if i > 5:
            #     break
            Ride.insert(
                event=Event.select().where(Event.name == row['Событие']),
                license=License.select().where(License.name == row['ТС'].replace(' ', '')),
                date=row['Начало'][:10]
            ).execute()


        # print(row['Заказчик'], row['СтатусЗаявки'])

    # for line in data_frame[:5]:
    #     print(line)

    # for el in data_frame['СтатусЗаявки']:
    #     if not OrderStatus.select().where(OrderStatus.name == el):
    #         Customer.insert(name=el).execute()


    # for el in data_frame['ВидОперации']:
    #     if not Service.select().where(Service.name == el):
    #         Service.insert(name=el).execute()

