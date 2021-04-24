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


## Set up and activate python environment

Install latest python:
```

python=python3.9
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update --ignore-missing
sudo apt install -y  $python-dev $python-venv
```

Download and install pip (package manager):
```
wget https://bootstrap.pypa.io/get-pip.py
$python get-pip.py
rm get-pip.py
``` 

Create and activate python environment:
```
$python -m venv venv
source venv/bin/activate
```

Download Project and install requirements:
```
sudo apt update
apt install git
git clone https://github.com/pip-install-HSE/TeploEnergoHackathon
pip install -r requirements.txt
```

## Set up .env variables

Сreate a .env file containing the bot configuration
```..env
DB_HOST = "0.0.0.0"
DB_USERNAME = "Sammy"
DB_PASSWORD = "qwerty123"
DB_PORT = "5432"
DB_NAME = "main_db"
```
