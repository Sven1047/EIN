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
    random_int = str(randint(1,1000))
    correct = False
    autor = []
    answer = ""
    if request.method == 'POST':
        conn = get_db_connection()

        query  = "SElECT zitate.zitat FROM zitate WHERE zitate.id = '" + random_int + "' "

        results = conn.execute(query).fetchall()

        query = "SELECT zitate.autor FROM zitate WHERE zitate.id = '" + random_int + "' "

        autor = conn.execute(query).fetchall()
        print(str(autor[0]))
        conn.close()

    if request.method == 'GET':
        answer = request.args.get("answer")

        if answer == autor:
            correct = True

    return render_template('index.html', results=results, autor=autor)

if __name__ == '__main__':
    app.run(debug=True, port=8086, use_reloader=False)