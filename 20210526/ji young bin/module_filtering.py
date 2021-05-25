import re 

'''
정규 표현식 메타 문자 

[] : 모든 문자 
() : 그룹화 및 추출패턴지정 
| : or 조건식 
. : \n(개행)을 제외한 모든 문자와 매칭 
* : 0회 이상 
+ : 1회 이상 
? : 0 or 1 
^ : 문자열 시작(단, [^]의 경우는 제외 의미임)
$ : 문자열의 끝 
\ : 메타 문자(이스케이프 문자)를 일반문자화 
{m,n} : m 이상 n 이하

/d : 숫자 
/D : 숫자가 아닌 것 
/s : whitespace(스페이스 , 탭, 개행)
/S : whitespace가 아닌 것 
/w : 문자 + 숫자(특수문자 아닌 것 . 단, '_'는 포함)
/W : 문자 + 숫자 아닌 것 
'''

'''
api호출이 비동기식이라서 api를 호출하면 어플도 동작이 되기 때문에 
api호출 과정에 필터링을 넣게되면 어플도 동작되는데 필터링 때문에 
signup과정에서 명령어가 들어가지 않기 때문에 오류가 생김 
'''

ban_spcial_char = ['_', '|', '[', ']', '=', '{', '}', ';', ':', ',', '<', '.', '>', '/', '\'','\"', '/', '(', ')']
use_spcial_char = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '?', '+']

#회원가입 과정에서 아이디가 조건에 맞는지 확인함
def idCheck(id):
    global ban_spcial_char

    if len(id) > 20: 
        print("아이디가 최대 길이를  넘었습니다..")
        return False

    elif len(id) < 5:
        print("아이디가 최소 길이를 넘지 못했습니다..")
        return False

    elif any(c in ban_spcial_char for c in id):
        print("아이디에 금지 문자가 포함 되어 있습니다.")
        return False

    else:
        print("아이디가 기준에 적합합니다.")
        return True

#회원가입 과정에서 비밀번호가 조건에 맞는지 확인함
def pwdCheck(pwd):
    global ban_spcial_char
    global use_spcial_char

    if len(pwd) > 20: 
        print("비밀번호가 최대 길이를  넘었습니다..")
        return False

    elif len(pwd) < 5:
        print("비밀번호가 최소 길이를 넘지 못했습니다..")
        return False

    elif any(c in ban_spcial_char for c in id):
        print("비밀번호에 금지 문자가 포함 되어 있습니다.")
        return False
    
    elif not any(c in use_spcial_char for c in id):
        print("비밀번호에 특수문자가 포함 되지 않았습니다.")
        return False

    else:
        print("비밀번호가 기준에 적합합니다.")
        return True
    
