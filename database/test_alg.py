from create_tables import *

if __name__ == '__main__':
    duration = 10
    ride = Ride.select().where(
        Ride.date == "12.01.2021" and
        Ride.license_id == License.select(License.id).where(License.name=="С963АМ1512")
    ).get()
    print(res.duration)
    Ride.update(duration=ride.duration+10).where(
        Ride.id == ride.id
    ).execute()
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