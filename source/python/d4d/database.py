import os
import records


def get_db_from_env():
    db_url = 'postgresql://{user}:{passwd}@{db_host}/{db}'.format(
        user=os.environ.get('DB_USER'),
        passwd=os.environ.get('DB_PASSWORD'),
        db_host=os.environ.get('DB_HOST'),
        db=os.environ.get('DB_NAME'))
    return records.Database(db_url)
