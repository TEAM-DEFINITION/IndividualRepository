def check(postcode):
    
    # 기존 가맹점 목록 불러오기
    # 1. db_store\\postcode 파일 불러오기
    f = open("db_store\\postcode","r", encoding="UTF8")
    # 2. 데이터 리스트 저장
    prev_block = f.readlines()
    f.close()

    # 포스트코드 찾기
    # 추출한 데이터에서 postcode값 확인
    for i in prev_block:
        if i.find(postcode) == -1: # 추출된 데이터에 postcode가 없는 경우
            pass
        else:
            # [ '00001|', '백화점|' ] -> [ '00001', '백화점' ] -> return 백화점
            return i.split("|")[1]
    return "NULL"