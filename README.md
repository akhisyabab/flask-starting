# Flask Starting
Flask starting app with flask

you can replace all name this project with new name
1. flask starting -> app name
2. flask_starting -> app_name
3. flask-starting - > app-name


# Table of contents
1. Get started without docker
2. Get started with docker


<hr>

## GET STARTED WITHOUT DOCKER:
#### create database and user on your local: 
```
CREATE DATABASE flask_starting;
CREATE DATABASE flask_starting_test;

CREATE USER flask_startinguser WITH password 'flask_startingpassword';
GRANT ALL PRIVILEGES ON database flask_starting to flask_startinguser;
ALTER USER flask_startinguser SUPERUSER;
```


#### Setup:
```sh
$ cd services/engine
$ virtualenv -p python3 ../../venv
$ source ../../venv/bin/activate
$ pip install -r requirements.txt
```

#### upgrade db for init data:
```
$ source ./scripts/dev_env.sh
$ flask db upgrade
```


#### Running:
```
$ source ./scripts/dev_env.sh
$ source ./scripts/run.sh
```
**open localhost:5000*

<hr><hr>

## GET STARTED WITH DOCKER
## Running :
**Dev:**
```sh
sudo ./scripts/run_dev.sh
```
**prod:**
```sh
sudo ./scripts/run_prod.sh
```

**Exec DB**
```sh
sudo ./scripts/engine-db.sh
psql -U postgres
```



