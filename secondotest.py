import tkinter as tk
import re


def is_password_secure(password):
    if len(password) < 7:
        return False

    if not any(c.isupper() for c in password):
        return False

    if not any(c.isdigit() for c in password):
        return False

    if not re.search(r'[!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:\'",<>\./?\\|]', password):
        return False

    return True


def check_password():
    password = entry.get()

    if is_password_secure(password):
        result_label.config(text="Password ok")
    else:
        result_label.config(text="La password non è sicura. Completa l'operazione e riprova.")


# Creazione della finestra principale
window = tk.Tk()
window.title("Verifica Password Sicura")

# Etichetta per istruzioni
instruction_label = tk.Label(window, text="Inserisci una password:")
instruction_label.pack()

# Campo di inserimento password
entry = tk.Entry(window, show="*")
entry.pack()

# Pulsante per verificare la password
check_button = tk.Button(window, text="Verifica Password", command=check_password)
check_button.pack()

# Etichetta per il risultato
result_label = tk.Label(window, text="")
result_label.pack()

# Esecuzione della finestra
window.mainloop()