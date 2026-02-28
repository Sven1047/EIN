from flask import Flask, render_template, request
import sqlite3
from random import *

correct_autor = ''
results = []

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('zitate.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    global correct_autor
    global results

    random_int = str(randint(1,1000))
    correct = False
    autor = []
    answer = ''

    if request.method == 'POST':
        results = []

        conn = get_db_connection()

        query  = "SElECT zitate.zitat FROM zitate WHERE zitate.id = '" + random_int + "' "

        results = conn.execute(query).fetchall()

        query = "SELECT zitate.autor FROM zitate WHERE zitate.id = '" + random_int + "' "

        autor = conn.execute(query).fetchall()

        for row in autor:
            correct_autor = f'{row[0]}'

        conn.close()

    if request.method == 'GET':
        answer = str(request.args.get("answer"))

        if answer.casefold() == correct_autor.casefold():
            correct = True

    return render_template('index.html', results=results, autor=autor, correct=correct, answer=answer)

if __name__ == '__main__':
    app.run(debug=True, port=8086, use_reloader=False)