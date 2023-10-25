import requests


def get_web_page_content(url):
    try:
        # Effettua una richiesta HTTP GET alla URL specificata
        response = requests.get(url)

        # Verifica se la richiesta ha avuto successo (status code 200)
        if response.status_code == 200:
            return response.text  # Restituisce il contenuto della pagina
        else:
            return f"Errore nella richiesta HTTP. Codice di stato: {response.status_code}"
    except Exception as e:
        return f"Errore durante la richiesta HTTP: {str(e)}"


def main():
    url = input("Inserisci l'URL della pagina web da scaricare: ")
    page_content = get_web_page_content(url)

    print("Contenuto della pagina:")
    print(page_content)


if __name__ == "__main__":
    main()
