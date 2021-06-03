## Flutter Part (updated 2021.06.03)

- 박성현 / 박민수 / 김주원 / 이선호 / 정규진

### 1. 비동기 처리

- FutureBuilder 사용 -> 비동기 처리
  	- Search tap
  	- Account tap

### 2. file_manage.dart

- 사용자 프로필에 사용될 문자열 추출용 함수 추가
  - chkIdx	-> 방문 x : 0 return
  - chkPlace -> 방문 x : 방문이 필요합니다 문자열 출력
- secure_storage에 사용되는 모든 키 값에 사용자의 id를 붙여 사용
  - userid : psh 일 때, key : psh_0 ~ psh_N
  - 사용자별 storage 구분에 필요

### 3. login_page.dart

- id / pw 정규식 적용

---------------------------------

### 1. home.dart

- 기존 코드

### 2. search.dart

- flutter_secure_storage 내에 저장된 데이터 목록화
- ListView로 구현
- 화면을 아래로 당겼을때 새로고침 되도록 RefreshIndicator 사용
- 목록 칸수를 최대 20개로 고정
  - 20개 이하 : 변화 없음
  - 20개 초과 : 가장 최근 목록부터 20개

### 3. account.dart

- 사용자의 프로필을 담아낼 레이아웃 구현
- 현재는 userid만 구현
- 추가적인 부분들은 회원가입시 입력하는 칸을 생성하여 받아올 필요 있음

