from flask import Flask, render_template, request
import sqlite3
from random import *

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('zitate.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        conn = get_db_connection()

        query  = "SElECT zitate.zitat FROM zitate WHERE zitate.id = '" + str(randint(1,1000)) + "' "

        results = conn.execute(query).fetchall()
        conn.close()

        print(results)

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, port=8086, use_reloader=False)

