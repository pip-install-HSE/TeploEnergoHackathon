from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomerChoice(models.TextChoices):
    CUSTOMER_1 = 'Аварийно-ремонтная служба', _('Аварийно-ремонтная служба')
    CUSTOMER_2 = 'Метрологическая служба', _('Метрологическая служба')
    CUSTOMER_3 = 'Управление материально-технического обеспечения', _('Управление материально-технического обеспечения')
    CUSTOMER_4 = 'Отдел диагностики и неразрушающего контроля', _('Отдел диагностики и неразрушающего контроля')
    CUSTOMER_5 = 'Электротехническая служба', _('Электротехническая служба')
    CUSTOMER_6 = 'Административно-хозяйственный отдел', _('Административно-хозяйственный отдел')
    CUSTOMER_7 = 'Ремонтная бригада РТС Сормовский', _('Ремонтная бригада РТС Сормовский')
    CUSTOMER_8 = 'РТС Сормовский', _('РТС Сормовский')
    CUSTOMER_9 = 'Ремонтно-механическая служба', _('Ремонтно-механическая служба')
    CUSTOMER_10 = 'Газовая служба', _('Газовая служба')
    CUSTOMER_11 = 'РТС Нижегородский', _('РТС Нижегородский')
    CUSTOMER_12 = 'РТС Ленинский', _('РТС Ленинский')
    CUSTOMER_13 = 'РТС Нагорный', _('РТС Нагорный')
    CUSTOMER_14 = 'Ремонтная бригада РТС Заречный', _('Ремонтная бригада РТС Заречный')
    CUSTOMER_15 = 'Ремонтная бригада РТС Нагорный', _('Ремонтная бригада РТС Нагорный')
    CUSTOMER_16 = 'РТС Заречный', _('РТС Заречный')
    CUSTOMER_17 = 'Легковой автопарк', _('Легковой автопарк')
    CUSTOMER_18 = 'Ремонтная бригада РТС Ленинский', _('Ремонтная бригада РТС Ленинский')
    CUSTOMER_19 = 'Ремонтная бригада РТС Нижегородский', _('Ремонтная бригада РТС Нижегородский')


class VehicleChoice(models.TextChoices):
    VEHICLE_1 = 'Грузопассажирские фургоны', _('Грузопассажирские фургоны')
    VEHICLE_2 = 'Грузовые специального назначения', _('Грузовые специального назначения')
    VEHICLE_3 = 'Грузовые самосвалы', _('Грузовые самосвалы')
    VEHICLE_4 = 'Экскаватор', _('Экскаватор')
    VEHICLE_5 = 'Грузовые цистерны', _('Грузовые цистерны')
    VEHICLE_6 = 'Грузовые бортовые', _('Грузовые бортовые')
    VEHICLE_7 = 'Трактор', _('Трактор')
    VEHICLE_8 = 'Самосвалы для перевозки грузов весом до 15 тонн', _('Самосвалы для перевозки грузов весом до 15 тонн')
    VEHICLE_9 = 'бочка', _('бочка')
    VEHICLE_10 = 'Автобусы общего назначения', _('Автобусы общего назначения')
    VEHICLE_11 = 'Грузовые седельный тягач', _('Грузовые седельный тягач')
    VEHICLE_12 = 'Грузовые фургоны', _('Грузовые фургоны')
    VEHICLE_13 = 'Погрузчик фронтальный', _('Погрузчик фронтальный')
    VEHICLE_14 = 'Автобусы малого класса', _('Автобусы малого класса')
    VEHICLE_15 = 'автовышка', _('автовышка')


class StaticAnalytics(models.Model):
    title = models.TextField()
    image_1 = models.ImageField(upload_to='images/', blank=True)
    image_2 = models.ImageField(upload_to='images/', blank=True)
    image_3 = models.ImageField(upload_to='images/', blank=True)


class AnalyticsResult(models.Model):
    image_link = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customer(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Event(models.Model):
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'event'


class License(models.Model):
    name = models.CharField(unique=True, max_length=16)

    class Meta:
        managed = False
        db_table = 'license'


class Order(models.Model):
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING)
    license = models.ForeignKey(License, models.DO_NOTHING, blank=True, null=True)
    predict_time = models.IntegerField()
    date = models.CharField(max_length=16)
    is_completed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'order'


class Ride(models.Model):
    event = models.ForeignKey(Event, models.DO_NOTHING)
    license = models.ForeignKey(License, models.DO_NOTHING, blank=True, null=True)
    date = models.CharField(max_length=16)
    real_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ride'


class SchemaTable(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
