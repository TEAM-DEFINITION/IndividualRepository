import hashlib
import binascii
import os
from endecrypt_test import AESCipher


block = ["DATA"]                                                    # 블록

def encrypt_test(key, data):                                        # 암호화
    encrypted_data = AESCipher(bytes(key)).encrypt(data) 
    print("encrypted_data is : ", encrypted_data)
    return encrypted_data

def decrypt_test(key, encrypted_data):                              # 복호화
    decrypted_data = AESCipher(bytes(key)).decrypt(encrypted_data)
    print("decrypted_data is : ", decrypted_data.decode('utf-8'))

def hashing_and_generate_key(block) :
    # hash_val=hashlib.sha256(str(block).encode()).hexdigest()
    hash_val = hashlib.sha256(str(block[-1]).encode()).digest()    # 이전 블록의 해시를 계산
    print("hash_val : ", hash_val)
    key = binascii.hexlify(bytearray(hash_val))[0:32]              # 그 해시로부터, 32바이트 key값 생성
    return key


while True:
    print("*********************************************************************************************************")
    print("block is : ", str(block))

    data = input("NEW DATA is : ")                                 # Client
    key = hashing_and_generate_key(block)
    encrypted_data = encrypt_test(key, data)        
    
    decrypt_test(key, encrypted_data)                              # Server
    block.append(data)



