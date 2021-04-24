sudo apt update

sudo apt install postgresql postgresql-contrib

sudo -i -u postgres

createuser --interactive

createdb admin
# reopen

passwd postgres

/etc/init.d/postgresql restart

nano /etc/postgresql/12/main/pg_hba.conf
ADD:
host    all             all              0.0.0.0/0                       md5
host    all             all              ::/0                            md5

nano /etc/postgresql/12/main/postgresql.conf
listen_addresses = '*'
/etc/init.d/postgresql restart

ALTER USER postgres PASSWORD 'newPassword'; 
