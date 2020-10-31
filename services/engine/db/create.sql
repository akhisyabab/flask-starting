CREATE DATABASE flask_starting;


CREATE USER flask_startinguser WITH password 'flask_startingpassword';
GRANT ALL PRIVILEGES ON database flask_starting to flask_startinguser;
ALTER USER flask_startinguser SUPERUSER;