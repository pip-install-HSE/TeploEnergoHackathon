from .create_tables import *

if __name__ == '__main__':
    date_info = '01.01.2021'
    license_info = 'О540УН1521'
    real_time = 10

    orders_data_frame = pd.read_excel(io='./orders.xlsx', sheet_name='Документы')
    orders_objects_frame = pd.read_excel(io='./orders.xlsx', sheet_name='ТЧ Объекты')
    orders_objects_numbers = orders_objects_frame['Номер']

    for i, row in orders_data_frame.iterrows():
    # for data in orders_data_frame[['Номер', 'АдресНазначения']]:
        number = row['Номер']
        el = row['АдресНазначения']
        # el = data['АдресНазначения']
        # if isinstance(el, float) and math.isnan(el):
        #     continue
        if number in orders_objects_numbers:
            el = orders_objects_frame.loc[orders_objects_frame['Номер'] == number]['Объект']
            print(number)

        else:
            pass
        # print(number, el)
            # el = orders_objects_frame['Объект']
        # if not License.select().where(License.name == el):
        #     License.insert(name=el).execute()

    # Event.insert(name='Работа').execute()

    # try:
    #     rides = Ride.select().where(
    #         Ride.license_id == License.select(License.id).where(License.name == license_info)
    #     )
    #     flag = False
    #     cur_ride = None
    #     for ride in rides:
    #         if ride.date == date_info:
    #             cur_ride = ride
    #             flag = True
    #             break
    #     if flag == False:
    #         print(0 / 0)
    #
    #     # print(f'"{ride.date}"')
    #     Ride.update(real_time=ride.real_time + real_time).where(
    #         Ride.id == cur_ride.id
    #     ).execute()
    #     # print("update")
    # except:
    #     # print(i, license_info, real_time)
    #     Ride.insert(
    #         event=Event.select().where(Event.name == 'Работа'),
    #         license=License.select().where(License.name == license_info),
    #         date=date_info,
    #         real_time=real_time
    #     ).execute()

    # print(res.exists())
    # try:
    # ride = Ride.select().join(License).where(
    #     # Ride.license.name == "С963АМ152" and
    #     (License.name == "С963АМ1521") and
    #     (Ride.date == "12.01.2021")
    # ).get()
    # print(ride)
    # # print(date_info, license_info, ride, type(ride))
    # ride.update(duration=ride.duration + duration).execute()
    # except:
    #     x = 10
    #     print("lol")
        # Ride.insert(
        #     event=Event.select().where(Event.name == row['Событие']),
        #     license=License.select().where(License.name == license_info),
        #     date=date_info,
        #     duration=duration
        # ).execute()
    # for x in data:
    #     print(x)