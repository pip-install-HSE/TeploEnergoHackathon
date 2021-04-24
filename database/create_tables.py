import os
from dotenv import load_dotenv
load_dotenv()
from peewee import *
import pandas as pd
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
    license = ForeignKeyField(License, null=False, backref='orders')
    is_completed = BooleanField(null=False)

# class Order(BaseModel):
#     numb

# class Tweet(BaseModel):
#     user = ForeignKeyField(User, backref='tweets')
#     message = TextField()
#     created_date = DateTimeField(default=datetime.datetime.now)
#     is_published = BooleanField(default=True)
db.connect(reuse_if_open=True)
tables = [Order, Customer, Vehicle, License]
for table in tables:
    try:
        db.drop_tables([table])
    except:
        print(f'Can not delete {table}')
db.create_tables(tables)

orders_data_frame = pd.read_excel(io='./orders.xlsx', sheet_name='Документы')

for el in orders_data_frame['Заказчик']:
    if not Customer.select().where(Customer.name == el):
        Customer.insert(name=el).execute()

for el in orders_data_frame['Требование_кТС']:
    if not Vehicle.select().where(Vehicle.name == el):
        Vehicle.insert(name=el).execute()

for el in orders_data_frame['НазначеноТС']:
    if not License.select().where(License.name == el):
        License.insert(name=el).execute()

for i, row in orders_data_frame.iterrows():
    if i > 5:
        break
    Order.insert(
        customer=Customer.select().where(Customer.name == row['Заказчик']),
        vehicle=Vehicle.select().where(Vehicle.name == row['Требование_кТС']),
        license=License.select().where(License.name == row['НазначеноТС']),
        is_completed=True if 'исполнен' in row['СтатусЗаявки'].lower() else False
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

