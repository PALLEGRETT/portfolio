def cifrario_cesare(parola, chiave):
    risultato = ""

    for i in range(len(parola)):
        char = parola[i]

        if (char.isupper()):
            risultato += chr((ord(char) + chiave - 65) % 26 + 65)
        else:
            risultato += chr((ord(char) + chiave - 97) % 26 + 97)

    return risultato

parola = input("Inserisci la parola: ")
chiave = int(input("Inserisci la chiave di cifratura (un numero): "))

print("Parola cifrata: ", cifrario_cesare(parola, chiave))