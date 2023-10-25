from flask import Flask, request, render_template

app = Flask(__name__)

def cifrario_cesare(parola, chiave):
    risultato = ""

    for i in range(len(parola)):
        char = parola[i]

        if (char.isupper()):
            risultato += chr((ord(char) + chiave - 65) % 26 + 65)
        else:
            risultato += chr((ord(char) + chiave - 97) % 26 + 97)

    return risultato

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        parola = request.form.get('parola')
        chiave = int(request.form.get('chiave'))
        risultato = cifrario_cesare(parola, chiave)
        return render_template('index1.html', risultato=risultato)
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)