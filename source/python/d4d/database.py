import os
import records
from pymongo import MongoClient

def get_pg_db_from_env():
    """Return a database connection to the Postgres database specified in docker.env"""
    db_url = 'postgresql://{user}:{passwd}@{db_host}/{db}'.format(
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWORD'),
        db_host=os.environ.get('DB_HOST'),
        db=os.environ.get('DB_NAME'))
    return records.Database(db_url)


def get_mongo_db_from_env():
    """Return a database connection to the Mongo database specified in docker.env"""
    return MongoClient(os.environ.get('MONGO_HOST'))
