def check(postcode): # postcode를 검사하는 함수

    ## 기존 가맹점 목록 불러오기
    # db_store 폴더의 postcode 파일을 읽기모드로 열어서 객체 f에 넣음
    f = open("db_store\\postcode", "r", encoding="UTF8")
    # 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트 prev_block을 선언
    prev_block = f.readlines()
    # 파일을 닫음
    f.close()

    ## 포스트 코드 찾기
    # for문을 돌면서 prev_block에서 해당 postcode를 찾음
    for i in prev_block:
        if i.find(postcode) == -1: # postcode와 다를 경우
            pass
        else: # postcode와 같을 경우
            # i를 |을 기준으로 나누어 두번째 값 리턴
            return i.split("|")[1]
            # ex) [00001|편의점|] -> [00001,편의점] -> 편의점
    return "NULL"