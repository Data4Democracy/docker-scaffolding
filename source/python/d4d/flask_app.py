from flask import Flask
from d4d.database import get_db_from_env

app = Flask(__name__)
db = get_db_from_env()


@app.route('/')
def hello_world():
    rows = db.query('SELECT salutation, instances FROM greeting')
    lines = []
    for r in rows:
        lines.append("{}: {}".format(r['salutation'], r['instances']))
        db.query('UPDATE greeting SET instances = :n WHERE salutation = :s',
                 s=r['salutation'],
                  n=r['instances'] + 1)

    return 'Flask Dockerized\n' + '\n'.join(lines)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
