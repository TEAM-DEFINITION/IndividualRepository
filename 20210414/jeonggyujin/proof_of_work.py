import time
import hashlib

def Proof_of_work(ver, previous_hash, MerkleRootHash, bits):
    nonce = 0
    time = time.time()
    hash_of_the_block = ""

    while((previous_hash > hash_of_the_block) or hash_of_the_block==""):
        nonce +=1
        data = (ver + MerkleRootHash + time + bits + nonce + previous_hash)
        hash_of_the_block = hashlib.sha512(data).hexdigest()

    return nonce
