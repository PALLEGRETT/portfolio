from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def password_checker():
    password = None
    is_secure = False

    if request.method == 'POST':
        password = request.form['password']

        # Esegui i controlli sulla password
        has_lowercase = any(c.islower() for c in password)
        has_uppercase = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{};:'\",<>/?.\|`~" for c in password)
        is_long_enough = len(password) >= 7

        # Verifica se la password è sicura
        is_secure = has_lowercase and has_uppercase and has_digit and has_special and is_long_enough

    return render_template('index.html', password=password, is_secure=is_secure)


if __name__ == '__main__':
    app.run(debug=True)