import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash


def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def create_genesis_block():
    return Block(0, "0", int(time.time()), "Blocco Genesis", calculate_hash(0, "0", int(time.time()), "Blocco Genesis"))


def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)


# Creazione della blockchain e aggiunta del blocco genesis
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Aggiunta di 4 blocchi alla blockchain
for i in range(1, 5):
    mozzarella_data = {
        "produttore": f"Produttore #{i}",
        "data_produzione": f"Data #{i}",
        "quantità": f"Quantità #{i}",
        "qualità": f"Qualità #{i}"
    }
    block_to_add = create_new_block(previous_block, mozzarella_data)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print(f"Blocco #{block_to_add.index} è stato aggiunto alla blockchain!")
    print(f"Dati Mozzarella: {block_to_add.data}")
    print(f"Hash: {block_to_add.hash}\n")
