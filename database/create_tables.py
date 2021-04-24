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

# class Service(BaseModel):
#     name = CharField(unique=True)

# class Order(BaseModel):

# class Order(BaseModel):
#     numb

# class Tweet(BaseModel):
#     user = ForeignKeyField(User, backref='tweets')
#     message = TextField()
#     created_date = DateTimeField(default=datetime.datetime.now)
#     is_published = BooleanField(default=True)
try:
    db.drop_tables([Customer])
except:
    print('Nothing to delete')
db.connect(reuse_if_open=True)
db.create_tables([Customer])

data_frame = pd.read_excel(io='./orders.xlsx', sheet_name='Документы')

for el in data_frame['Заказчик']:
    if not Customer.select().where(Customer.name == el):
        Customer.insert(name=el).execute()

# for el in data_frame['ВидОперации']:
#     if not Service.select().where(Service.name == el):
#         Service.insert(name=el).execute()

