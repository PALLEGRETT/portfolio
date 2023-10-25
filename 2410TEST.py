from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return f'Ciao {username}! Benvenuto di nuovo.'
    else:
        return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    if username:
        response = make_response(f'Login effettuato come {username}.')
        response.set_cookie('username', username)
        return response
    else:
        return 'Nome utente mancante. Impossibile effettuare il login.'


@app.route('/logout')
def logout():
    response = make_response('Logout effettuato.')
    response.set_cookie('username', '', expires=0)
    return response


if __name__ == '__main__':
    app.run()
