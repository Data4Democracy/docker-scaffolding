from flask import Flask, g, render_template
from d4d.database import get_pg_db_from_env, get_mongo_db_from_env

app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    Show all of the greetings from either DB, and increment each greeting by one
    """
    pg = get_pg_db()
    rows = pg.query('SELECT salutation, instances FROM greeting')
    greetz = []
    for r in rows:
        greetz.append(r)
        pg.query('UPDATE greeting SET instances = instances + 1 WHERE salutation = :s', s=r['salutation'])

    mongo = get_mongo_db()
    docs = mongo.project.greeting.find({})
    for d in docs:
        greetz.append(d)
        mongo.project.greeting.update({'salutation': d['salutation']},
                                      {'$inc': {'instances': 1}})
    app.logger.info(greetz)

    return render_template('greeting.html', greetz=greetz)


def get_pg_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'pg'):
        g.pg = get_pg_db_from_env()
    return g.pg

def get_mongo_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'mongo'):
        g.mongo = get_mongo_db_from_env()
    return g.mongo

@app.teardown_appcontext
def close_db(error):
    """Closes the databases at the end of the request."""
    if hasattr(g, 'pg'):
        g.pg.close()
    if hasattr(g, 'mongo'):
        g.mongo.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
