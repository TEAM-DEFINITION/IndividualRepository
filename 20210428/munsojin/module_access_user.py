import hashlib
import module_endecrypt
import ast
import time
import os



'''

[db_user]
FileName : {{userId}}_db

[variable]
USER_ID:str
USER_PASSWORD:str
DATA:str
PREV_HASH:str

'''

class USER :
    def __init__(self):
        pass

    def login(self, userId, userPwd):

        if os.path.isfile("./db_user/" + userId +"_db") == False :
            return 401


        f = open("db_user\\" + userId + "_db","r", encoding="UTF8")
        temp = f.readlines()
        f.close()
        print( temp[1].split("|")[0])
        if temp[1].split("|")[1] == userPwd :
            return 200
        else :
            return 402
    
    def genesisBlockCreate(self, userId, userPwd, clientrandom):

        # 중복확인
        if os.path.isfile("./db_user/" + userId +"_db") :
            return 401
        
        genesisBlock = userId + "|" + userPwd +  "|" + clientrandom +"|"
        genesisBlock = genesisBlock + hashlib.sha512(genesisBlock.encode('utf-8')).hexdigest() +"|"

        f = open("db_user\\" + userId + "_db","w", encoding="UTF8" )
        f.write("\n" + genesisBlock)
        f.close()

        return 200


    def nextBlockCreate(self, userId, userPwd, data):

        # 이전 블록 읽어오기
        f = open("db_user\\" + userId + "_db","r", encoding="UTF8")
        prevBlock = f.readlines()
        f.close()

        # 이전 블록의 해시값을 사용자 블록에 쓰기
        prevData = prevBlock[-1]
        result, place, time = module_endecrypt.FERCIPHER(prevData.split("|")[3]).decrypt(data)
        newBlock = result + hashlib.sha512(prevData.encode('utf-8')).hexdigest() + "|"
        f = open("db_user\\" + userId + "_db","a", encoding="UTF8")
        f.write("\n" + newBlock)
        f.close()

        # 서버 블록 포맷
        serverBlock = "HybridAccessServer|" + place + "|" + time + "|"

        # 새로운 블록을 쓰기 위해 수정된 체인 읽기
        f = open("db_user\\" + userId + "_db","r", encoding="UTF8")
        prevBlock = f.readlines()
        f.close()

        # 사용자 블록의 해시값을 추출하여 추가
        prevData = prevBlock[-1]
        serverBlock = serverBlock + hashlib.sha512(prevData.encode('utf-8')).hexdigest() + "|"
        f = open("db_user\\" + userId + "_db","a", encoding="UTF8")
        f.write("\n" + serverBlock)
        f.close()

        # 최종 체인의 정보를 읽어옴
        f = open("db_user\\" + userId + "_db","r", encoding="UTF8")
        prevBlock = f.readlines()
        f.close()

        # 보낼 데이터를 n-1번째 체인의 해시값으로 암호화
        result = module_endecrypt.FERCIPHER(prevBlock[-2].split("|")[3]).encrypt(serverBlock)
        return result
