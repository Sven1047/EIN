from flask import Flask, render_template, request
import sqlite3
from random import *

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('zitate.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST', 'SUBMIT'])
def index():
    results = []
    random = str(randint(1,1000))
    correct = False
    autor = []
    if request.method == 'POST':
        conn = get_db_connection()

        query  = "SElECT zitate.zitat FROM zitate WHERE zitate.id = '" + random + "' "

        results = conn.execute(query).fetchall()
        conn.close()

    elif request.method == 'SUBMIT':
        answer = request.form.get('answer','').strip()

        print(answer)

        conn = get_db_connection()

        query = "SELECT zitate.autor FROM zitate WHERE zitate.id = '" + random + "' "

        autor = conn.execute(query).fetchall()
        conn.close()

        print(autor)

        if answer == autor:
            correct = True

    print(autor)
    return render_template('index.html', results=results, autor=autor)

if __name__ == '__main__':
    app.run(debug=True, port=8086, use_reloader=False)

