from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Eine einfache Liste für alles
CHAT_VERLAUF = ["Hallo! Wie kann ich helfen?"]

# die möglichen Antworten des Bots
BOT_STATEMENTS = [
    "Interessant. Erzählen Sie mir mehr darüber.",
    "Du meine Güte... Wie fühlen Sie sich dabei?",
    "Interessant. Was löst das in Ihnen aus?",
    "Das ist bestimmt nicht einfach... Und weiter?",
    "Interessant. Haben Sie das schon öfter erlebt?",
    "Verstehe... Was bedeutet das für Sie?",
    "Interessant. Wie gehen Sie damit um?",
    "Verstehe... führen Sie das bitte weiter aus."
]

@app.route('/', methods=['GET', 'POST'])
def chat_seite():
    global CHAT_VERLAUF
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'senden':
            user_text = request.form.get('nachricht')

            # wir prüfen ob diese nicht leer ist
            if user_text.strip() != "":
                CHAT_VERLAUF.append(user_text)

                if "Freude" in user_text:
                    antwort = "☺️"
                else:
                    zufall_index = random.randint(0, len(BOT_STATEMENTS) - 1)
                    antwort = BOT_STATEMENTS[zufall_index]

                # diese wird dem Chat-Verlauf angefügt mit append
                CHAT_VERLAUF.append(antwort)

        elif action == 'löschen':
            CHAT_VERLAUF = ["Hallo! Wie kann ich helfen?"]
            
    return render_template('index.html', verlauf=CHAT_VERLAUF)

if __name__ == '__main__':
    # port 8086 wie bei dir, debug=True hilft Fehler zu finden
    app.run(debug=True, port=8086,use_reloader=False)


    