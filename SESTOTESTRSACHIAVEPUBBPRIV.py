from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Genera una coppia di chiavi per Bob
private_key_bob = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key_bob = private_key_bob.public_key()

# Salva la chiave pubblica di Bob in un file
pem = public_key_bob.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open('public_key.pem', 'wb') as f:
    f.write(pem)

# Lisa cifra un messaggio con la chiave pubblica di Bob
message = b"messaggio segreto"
ciphertext = public_key_bob.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Messaggio cifrato:", ciphertext)
