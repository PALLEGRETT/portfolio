import socket

def scan_ports(target, ports):
    open_ports = []
    for port in ports:
        try:
            # Crea un oggetto socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Imposta un timeout per la connessione
            s.settimeout(1)
            # Prova a connettersi alla porta
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        except Exception:
            pass
    return open_ports

def main():
    target = input("Inserisci l'indirizzo IP da scannerizzare: ")
    ports = range(1, 1025)  # Scansiona le porte da 1 a 1024 (puoi personalizzare questo intervallo)
    open_ports = scan_ports(target, ports)

    if open_ports:
        print("Porte aperte su", target, ":")
        for port in open_ports:
            print(port)
    else:
        print("Nessuna porta aperta trovata su", target)

if __name__ == "__main__":
    main()
