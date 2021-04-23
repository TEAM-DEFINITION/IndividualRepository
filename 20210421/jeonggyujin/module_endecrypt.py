import os, hashlib
from cryptography.fernet import Fernet
import base64
#import ast
import json
import module_postcode
import datetime



'''

Encrypt Mode : Fernet
Decrypt Mode : Fernet

Key size : 32bytes

'''
class FerCipher:

    # 키를 사용하기위해 만드는 로직
    def __init__(self, key):
        self.key = key
        # 키 파싱
        #32자리의 길이까지 자르고 인코딩해서 key에 저장
        self.key = self.key[:32].encode('utf-8')
        print("키변환" + str(self.key))
        # 키값을 base64인코딩(바이너리 데이터를 아스키로 변환하는 것)
        self.key = base64.urlsafe_b64encode(self.key)
        print("키변환끝" + str(self.key))

    # 클라이언트에게 보낼 키를 암호화
    def encrypt(self, data):
        print("암호화 키값 : " + str(self.key))
        print("암호화할 데이터 : " + data)
        # 키를 대칭키암호화하여 cipher_suite 에저장
        cipher_suite = Fernet(self.key)
        # cipher_suite값을 인코딩하여 cipher_text에 저장
        cipher_text = cipher_suite.encrypt(data.encode())
        print("보낼 암호문 : " + cipher_text.decode('utf-8'))
        return cipher_text

    # 클라이언트에게 받은 키를 복호화
    def decrypt(self, data):
        print("복호화 키값 : " + str(self.key))
        print("복호화할 데이터 : " + str(data.encode()))
        # 키를 대칭키암호화하여 cipher_suite 에저장
        cipher_suite = Fernet(self.key)
        # 클라이언트로부터 받은 데이터를 복호화해 plain_text에 저장
        plain_text = cipher_suite.decrypt(data.encode())
        print("유저로부터 받은 데이터 : " + str(plain_text))

        # 주소확인 테스팅 시작!!
        print("사용자가 방문할 장소 : " + module_postcode.check(plain_text.decode('utf-8').split("|")[2]))
        # 클라이언트로부터 받은데이터, 포스트코드에 등록된 기관, 타임스탬프 를 리턴
        return plain_text.decode('utf-8'), module_postcode.check(plain_text.decode('utf-8').split("|")[2]), str(datetime.datetime.now())

