#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER d4d WITH PASSWORD 'democracy';
    CREATE DATABASE project;
    GRANT ALL PRIVILEGES ON DATABASE project TO d4d;
EOSQL

psql -v ON_ERROR_STOP=1 --username d4d project <<-EOSQL
    CREATE TABLE greeting (
        id SERIAL PRIMARY KEY,
        salutation TEXT NOT NULL,
        instances INT DEFAULT 0
    );

    INSERT INTO greeting (salutation) VALUES ('Hello');
EOSQL
