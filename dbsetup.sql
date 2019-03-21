

DROP DATABASE IF EXISTS finalproject; 

CREATE DATABASE finalproject; 

DROP USER IF EXISTS finalproject; 

CREATE USER finalproject WITH PASSWORD 'finalproject'; 

GRANT ALL PRIVILEGES ON DATABASE finalproject TO finalproject; 

ALTER USER finalproject SET search_path = data;


