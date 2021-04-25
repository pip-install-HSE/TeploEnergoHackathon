import os
from tqdm import tqdm
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

class Address(BaseModel):
    name = CharField(null=False, unique=True)
# class Service(BaseModel):
#     name = CharField(unique=True)

class Order(BaseModel):
    customer = ForeignKeyField(Customer, null=False, backref='orders')
    vehicle = ForeignKeyField(Vehicle, null=False, backref='orders')
    license = ForeignKeyField(License, null=True, backref='orders')
    predict_time = IntegerField(null=False)
    date = CharField(null=False, max_length=16)
    address = ForeignKeyField(Address, null=False, backref='orders')
    is_completed = BooleanField(null=False)
    is_address_match = BooleanField(null=True)

class Event(BaseModel):
    name = CharField(null=False, unique=True, max_length=64)

class Ride(BaseModel):
    event = ForeignKeyField(Event, null=False, backref='rides')
    license = ForeignKeyField(License, null=True, backref='rides')
    date = CharField(null=False, max_length=16)
    real_time = IntegerField(null=False)

    # class Meta:
    #     indexes = (
    #         (('license', 'date'), True)
    #     )
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

    orders_data_frame = pd.read_excel(io='./orders.xlsx', sheet_name='Документы')
    orders_objects_frame = pd.read_excel(io='./orders.xlsx', sheet_name='ТЧ Объекты')

    for el in tqdm(orders_data_frame['Заказчик'], total=orders_data_frame.shape[0]):
        if not Customer.select().where(Customer.name == el):
            Customer.insert(name=el).execute()

    for el in tqdm(orders_data_frame['Требование_кТС'], total=orders_data_frame.shape[0]):
        if not Vehicle.select().where(Vehicle.name == el):
            Vehicle.insert(name=el).execute()

    for el in tqdm(orders_data_frame['НазначеноТС'], total=orders_data_frame.shape[0]):
        if isinstance(el, float) and math.isnan(el):
            continue
        if not License.select().where(License.name == el):
            License.insert(name=el).execute()

    for i, row in tqdm(orders_data_frame.iterrows(), total=orders_data_frame.shape[0]):
        # if i > 5:
        #     break
        is_completed = row['СтатусЗаявки']
        if isinstance(is_completed, float) and math.isnan(is_completed):
            continue
        is_completed = True if 'исполнен' in is_completed.lower() else False
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
                    delta_time = 24 * 60

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
            predict_time=delta_time,
            date=row['ДатаВыполненияС'][:10],
            is_completed=is_completed
        ).execute()
        # print(start_time)
        # print(end_time)
        # print()

    rides_data_frame = pd.read_excel(io='./rides.xlsx', sheet_name='Поездки по данным GPS')

    for el in tqdm(rides_data_frame['Событие'], total=rides_data_frame.shape[0]):
        if not Event.select().where(Event.name == el):
            Event.insert(name=el).execute()

    for i, row in tqdm(rides_data_frame.iterrows(), total=rides_data_frame.shape[0]):
        if row['Событие'] != 'Работа':  # everything is broken if you remove it.
            continue

        # if i > 5:
        #     break
        license_info = row['ТС'].replace(' ', '')
        date_info = row['Начало'][:10]
        real_time = row['Длительноcть']
        if isinstance(real_time, float) and math.isnan(real_time):
            continue
        real_time = int(real_time[0:2]) * 60 + int(real_time[3:5])

        try:
            rides = Ride.select().where(
                Ride.license_id == License.select(License.id).where(License.name == license_info)
            )
            flag = False
            cur_ride = None
            for ride in rides:
                if ride.date == date_info:
                    cur_ride = ride
                    flag = True
                    break
            if flag == False:
                print(0 / 0)

            # print(f'"{ride.date}"')
            Ride.update(real_time=cur_ride.real_time + real_time).where(
                Ride.id == cur_ride.id
            ).execute()
            # print("update")
        except:
            # print(i, license_info, real_time)
            Ride.insert(
                event=Event.select().where(Event.name == 'Работа'),
                license=License.select().where(License.name == license_info),
                date=date_info,
                real_time=real_time
            ).execute()






        # Ride.insert(
        #     event=Event.select().where(Event.name == row['Событие']),
        #     license=License.select().where(License.name == license_info),
        #     date=date_info,
        #     real_time=real_time
        # ).execute()
        # dur = Ride.select(Ride.duration).where(
        #     Ride.license.name == license_info and
        #     Ride.date == date_info
        # ).execute()
        # if dur is None:
        #     Ride.insert(
        #         event=Event.select().where(Event.name == row['Событие']),
        #         license=license_info,
        #         date=date_info,
        #         duration=duration
        #     ).execute()
        # else:
        #     Ride.update(duration=duration+1).where(
        #         Ride.license.name == license_info and
        #         Ride.date == date_info
        #     )
            # x = Ride.update(duration=ride[1]+duration).where(
            #     Ride.license.name == license_info and
            #     Ride.date == date_info
            # ).execute()


    # print(row['Заказчик'], row['СтатусЗаявки'])

# for line in data_frame[:5]:
#     print(line)

# for el in data_frame['СтатусЗаявки']:
#     if not OrderStatus.select().where(OrderStatus.name == el):
#         Customer.insert(name=el).execute()


# for el in data_frame['ВидОперации']:
#     if not Service.select().where(Service.name == el):
#         Service.insert(name=el).execute()

