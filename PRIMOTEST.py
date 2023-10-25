import re


def is_password_secure(password):
    # Verifica la lunghezza minima
    if len(password) < 7:
        return False

    # Verifica la presenza di almeno una lettera maiuscola
    if not any(c.isupper() for c in password):
        return False

    # Verifica la presenza di almeno un numero
    if not any(c.isdigit() for c in password):
        return False

    # Verifica la presenza di almeno un carattere speciale
    if not re.search(r'[!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:\'",<>\./?\\|]', password):
        return False

    return True


while True:
    password = input("Inserisci una password: ")

    if is_password_secure(password):
        print("Password ok")
        break
    else:
        print("La password non è sicura. Completa l'operazione e riprova.")
