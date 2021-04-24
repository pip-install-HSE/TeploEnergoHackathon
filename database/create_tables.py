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
    name = CharField(unique=True)

class Service(BaseModel):
    name = CharField(unique=True)
# class Order(BaseModel):
#     numb

# class Tweet(BaseModel):
#     user = ForeignKeyField(User, backref='tweets')
#     message = TextField()
#     created_date = DateTimeField(default=datetime.datetime.now)
#     is_published = BooleanField(default=True)
db.drop_tables([Customer, Service])
db.connect(reuse_if_open=True)
db.create_tables([Customer, Service])

data_frame = pd.read_excel(io='./orders.xlsx', sheet_name='Документы')
for el in data_frame['Заказчик']:

    if el not in Customer.select(Customer.name):
        Customer.insert(name=el).execute()


