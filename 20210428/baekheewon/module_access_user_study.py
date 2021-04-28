import hashlib
import module_endecrypt_study
import ast
import time
import os



'''

[db_user]
FileName : {{user_id}}_db

[variable]
USER_ID:str
USER_PASSWORD:str
DATA:str
PREV_HASH:str

'''

# user의 정보를 관리하는 클래스
class user :
    def __init__(self):
        pass
    

    # user의 로그인 정보를 확인하는 함수
    def login(self, user_id, user_pwd):
        
        # user_id가 없을 경우
        # isfile()함수: 파일을 검사하는 함수, 파일이 존재하지 않거나 디렉토리라면 false 반환
        if os.path.isfile("./db_user/" + user_id +"_db") == False : 
            return 401

        f = open("db_user\\" + user_id + "_db","r", encoding="UTF8")
        temp = f.readlines()
        f.close()
        print(temp[1].split("|")[0]) # user_id 출력

        # user_pwd 비교
        if temp[1].split("|")[1] == user_pwd : 
            return 200
        else :
            return 402


    # 회원가입시 제네시스 블록을 만드는 함수
    def genesis_block_create(self, user_id, user_pwd, clientrandom):

        ## 중복확인
        # 이미 있는 회원이라면 401 리턴
        if os.path.isfile("./db_user/" + user_id +"_db") :
            return 401
        
        # 제네시스 블록 생성
        # 형태: [user_id|user_pwd|clientrandom|해시값|]
        genesis_block = user_id + "|" + user_pwd +  "|" + clientrandom +"|"
        genesis_block = genesis_block + hashlib.sha512(genesis_block.encode('utf-8')).hexdigest() +"|"

        # 해당 user의 파일을 생성하고 제네시스 블록을 추가
        f = open("db_user\\" + user_id + "_db","w", encoding="UTF8" )
        f.write("\n" + genesis_block)
        f.close()

        return 200 # 성공


    # 다음 블록 생성 함수
    # module_start_study.py를 보면 data는 postcode를 의미
    def next_block_create(self, user_id, user_pwd, data):

        ## 이전 블록 읽어오기
        f = open("db_user\\" + user_id + "_db","r", encoding="UTF8")
        prev_block = f.readlines()
        f.close()

        ## 이전 블록의 해시값을 사용자 블록에 쓰기
        # 가장 최근 이전 블록을 prev_data로 정의
        prev_data = prev_block[-1]
        # 제네시스 형태: [user_id|user_pwd|clientrandom|해시값|]
        # prev_data.split("|")[3] = 해시값 -> 해시값으로 postcode를 decrypt함
        result, place, time = module_endecrypt_study.FerCipher(prev_data.split("|")[3]).decrypt(data)
        new_block = result + hashlib.sha512(prev_data.encode('utf-8')).hexdigest() + "|"
        f = open("db_user\\" + user_id + "_db","a", encoding="UTF8")
        f.write("\n" + new_block)
        f.close()

    #...
