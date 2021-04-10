import hashlib, os, base64
from Cryptodome.Cipher import AES


def gen_sha256_hashed_key_salt(key):
    salt1 = hashlib.sha256(key.encode()).digest()
    return hashlib.sha256(salt1+key.encode()).digest()


def encrypt(data, key):
    BS = 16
    pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)
    raw = pad(data)
    key = gen_sha256_hashed_key_salt(key)
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + encryptor.encrypt(raw.encode('utf-8')))


def decrypt(enc, key):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    key = gen_sha256_hashed_key_salt(key)
    decryptor = AES.new(key, AES.MODE_CBC, iv[:16])
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    return unpad(decryptor.decrypt(enc[16:]))


if __name__ == '__main__':
    # print(gen_sha256_hashed_key_salt('hi'))
    data = 'd'
    key = 'dff'
    print(encrypt(data,key))
    print(decrypt(encrypt(data,key),key))

            # mymac = bytearray.fromhex('{:012X}'.format(int(k, 16)))
    # print(len(os.urandom(16)))
    # print(len(gen_sha256_hashed_key_salt('hi')))
    # server_block = [
    #     "K-Shield Jr. DEFINITION TEAM",
    #     "2BD1144CFFE6D3A71A85B1ECFFE4D4EFA50EAD8186731E7FC8EE42FB4F814CE4C31E721FFE9F6DC9D4B2585F15F570045FC6A94EED99A1779E97C64142D3CF41",
    #     "Authentiacation Complete!!"
    # ]
    # a=[[] for _ in range(20)]
    #
    # print(a)
    # a=str(encrypt(server_block, key))
    # print(a)
    # print(decrypt(a, key))