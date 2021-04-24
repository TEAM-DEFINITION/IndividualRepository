# 참조: https://somjang.tistory.com/entry/Python-Python%EA%B3%BC-cryptography%EB%A5%BC-%ED%86%B5%ED%95%B4-%EB%8C%80%EC%B9%AD%ED%82%A4-%EC%95%94%ED%98%B8%ED%99%94-%ED%95%98%EA%B8%B0

import os, hashlib
from cryptography.fernet import Fernet # 대칭키 암호화
import base64
#import ast
import json
import module_postcode_study
import datetime


'''

Encrypt Mode : Fernet
Decrypt Mode : Fernet

Key size : 32bytes

'''

class FerCipher:

    def __init__(self, key): # 객체를 초기화하는 함수
        self.key = key
        ## 키 파싱
        # key 32개의 문자만 encoding하여 self.key에 넣는다.
        self.key = self.key[:32].encode('utf-8')
        print("키변환" + str(self.key))
        # 키를 base64 인코딩한다.
        self.key = base64.urlsafe_b64encode(self.key)
        print("키변환끝" + str(self.key))

    # 서버가 클라이언트에게 줄 데이터를 암호화
    def encrypt(self, data): # 암호화 함수
        print("암호화 키값 : " + str(self.key))
        print("암호화할 데이터 : " + data)
        # 키를 대칭키 암호화하여 cipher_suite를 선언한다.
        cipher_suite = Fernet(self.key)
        # data를 키로 암호화하고 cipher_text를 선언한다.
        cipher_text = cipher_suite.encrypt(data.encode())
        print("보낼 암호문 : " + cipher_text.decode('utf-8'))
        return cipher_text

    # 클라이언트가 서버에게 준 데이터를 복호화
    def decrypt(self, data): # 복호화 함수
        print("복호화 키값 : " + str(self.key))
        print("복호화할 데이터 : " + str(data.encode()))
        # 키를 대칭키 암호화하여 cipher_suite를 선언한다.
        cipher_suite = Fernet(self.key)
        # data를 키로 복호화하고 plain_text를 선언한다.
        plain_text = cipher_suite.decrypt(data.encode())
        print("유저로부터 받은 데이터 : " + str(plain_text))

        ## 주소 확인 테스팅 시작!!
        # plain_text의 2번째에 있는 postcode를 module_postcode_study의 check함수를 사용하여 장소를 출력한다.
        print("사용자가 방문할 장소 : " + module_postcode_study.check(plain_text.decode('utf-8').split('|')[2]))

        # 클라이언트가 준 데이터, postcode에 해당하는 장소, 시간을 리턴한다.
        return plain_text.decode('utf-8'), module_postcode_study.check(plain_text.decode('utf-8').split("|")[2]), str(datetime.datetime.now())
