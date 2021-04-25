-- select * from "ride"
-- inner join "order" on ride.license_id = "order".id
-- WHERE ride.license_id = 3;
-- select * from "order";

-- l.name, o.date, "order".predict_time, o.real_time
select l.name, o.date, "order".predict_time, o.real_time, c.name, v.name from "order"
inner join customer c on c.id = "order".customer_id
inner join vehicle v on v.id = "order".vehicle_id
-- inner join customer
-- inner join event
inner join license l on l.id = "order".license_id
inner join "ride" o on l.id = o.license_id and "order".date = o.date;
-- where (upper(trim(o.date)) = upper(trim('17.01.2021')));

select count(*) from "order";

select count(*) from "ride";

-- select * from ride
-- -- inner join license l on ride.license_id = l.id
-- where ride.license_id = ;

-- select count(*) from "ride"
-- where (upper(trim(ride.date)) = upper(trim('04.01.2021')));

-- select * from "ride";