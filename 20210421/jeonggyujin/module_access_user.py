import hashlib
import module_endecrypt
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

class user :
    def __init__(self):
        pass

    # 파일의 유무를 판별해 사용자의 로그인에 대해 응답하는 로직
    def login(self, user_id, user_pwd):

        # isfile()은 지정한 path가 존재하는 파일이면 true반환 없으면 false반환
        # 서버는 해당하는 계정마다 ./db_user/"user_id"/_db 형식으로 파일을 만들어 존재하는 계정인지를 확인한다.
        if os.path.isfile("./db_user/" + user_id +"_db") == False :
            return 401 # Unauthorized 반환

        # 위의 조건문에 안걸렸다면 해당 파일이 존재했다는 의미 이므로 해당하는 파일을 인코딩해서 읽기모드로 열어옴
        f = open("db_user\\" + user_id + "_db","r", encoding="UTF8")
        # 파일의 내용을 불러와서 파일의 라인마다 temp의 리스트에 한줄씩 저장한다.
        temp = f.readlines()
        # 파일닫음
        f.close()
        # temp[1]안에있는 데이터에 단어별로 | 을 사용해 문자열을 나누어 출력. =(a|b|c)
        print( temp[1].split("|")[0])
        # temp[1][1] 값과 사용자가 입력한 pwd값을 비교
        if temp[1].split("|")[1] == user_pwd :
            return 200 # ok
        else :
            return 402 # Payment Required
    
    # 아이디에 해당하는 제네시스 블록을 생성하는 로직
    def genesis_block_create(self, user_id, user_pwd, clientrandom):

        # 중복확인
        # 해당 파일이 존재하면 401리턴
        if os.path.isfile("./db_user/" + user_id +"_db") :
            return 401 # 요청실패
        
        # 데이터를 해당 형식으로 genesis_block 변수에 저장
        # user_id | user_pwd | clientrandom | 앞의 값(user_id | user_pwd | clientrandom |)을 인코딩후 해시암호화한 값 |
        genesis_block = user_id + "|" + user_pwd +  "|" + clientrandom +"|"
        genesis_block = genesis_block + hashlib.sha512(genesis_block.encode('utf-8')).hexdigest() +"|"

        # 사용자의 파일을 쓰기모드로 열고, 다음줄에 위에 생성한 제네시스블록변수값을 넣고 파일닫음.
        f = open("db_user\\" + user_id + "_db","w", encoding="UTF8" )
        f.write("\n" + genesis_block)
        f.close()

        return 200 # 요청성공


    def next_block_create(self, user_id, user_pwd, data):

        # 이전 블록 읽어오기
        # 사용자 파일에있는 데이터를 prev_block 변수에 리스트형식으로 저장
        f = open("db_user\\" + user_id + "_db","r", encoding="UTF8")
        prev_block = f.readlines()
        f.close()

        # 이전 블록의 해시값을 사용자 블록에 쓰기
        # prev_block = ['user_id', 'user_pw', 'genesis', '현재좌표']
        # prev_block[-1] = 마지막 블록에 저장한 해시 값을 prev_data변수에 저장
        prev_data = prev_block[-1]
        # module_endecryp.py의 FerCiper 클래스를 이용해 prevdata변수를 split을 이용해 | 를 제거하고 [3]블록인 '이전 블록을 해시암호화한값' 을 postnum코드값을 이용해 복호화한다.
        # 복호화한 값은 result 변수에 저장한다.
        result, place, time = module_endecrypt.FerCipher(prev_data.split("|")[3]).decrypt(data)
        # 복호화한 데이터와, prev_data를 인코딩하여 해시암호화 한 값을 더한 후 에 끝에 |를 추가한 값을 new_block에 넣는다.
        new_block = result + hashlib.sha512(prev_data.encode('utf-8')).hexdigest() + "|"
        # 사용자의 파일을 append 모드로 불러온다.
        f = open("db_user\\" + user_id + "_db","a", encoding="UTF8")
        # 개행후 new_block을 파일에 저장한다.
        f.write("\n" + new_block)
        # ['user_id', 'user_pw', 'genesis', 'new_block']
        f.close()

        # 서버 블록 포맷
        server_block = "HybridAccessServer|" + place + "|" + time + "|"

        # 새로운 블록을 쓰기 위해 수정된 체인 읽기
        f = open("db_user\\" + user_id + "_db","r", encoding="UTF8")
        # prev_block = ['user_id', 'user_pw', 'genesis', 'new_block']
        prev_block = f.readlines()
        f.close()

        # 사용자 블록의 해시값을 추출하여 추가
        # prev_block = ['user_id', 'user_pw', 'genesis', 'new_block', 현재좌표]
        prev_data = prev_block[-1] # new_block 저장
        # server_block = 'server_block + hash(prev_data)' | 
        server_block = server_block + hashlib.sha512(prev_data.encode('utf-8')).hexdigest() + "|"
        f = open("db_user\\" + user_id + "_db","a", encoding="UTF8")
        f.write("\n" + server_block)
        # 'user_id' | 'user_pw' | 'genesis' | 'new_block' | server_block |
        f.close()

        # 최종 체인의 정보를 읽어옴
        f = open("db_user\\" + user_id + "_db","r", encoding="UTF8")
        # prev_block = ['|user_id|', '|user_pw|', '|genesis|', '|new_block|', '|server_block|']
        prev_block = f.readlines()
        f.close()

        # 보낼 데이터를 n-1번째 체인의 해시값으로 암호화
        result = module_endecrypt.FerCipher(prev_block[-2].split("|")[3]).encrypt(server_block)
        # new_block '|' 제거 후 [][3] 값을 서버블록으로 암호화
        return result