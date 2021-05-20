## Flutter Part

- 박성현 / 박민수 / 김주원 / 이선호 / 정규진

### - home.dart

- 기존 코드

### - search.dart

- flutter_secure_storage 내에 저장된 데이터 목록화
- ListView로 구현
- 화면을 아래로 당겼을때 새로고침 되도록 RefreshIndicator 사용
- 목록 칸수를 최대 20개로 고정
  - 20개 이하 : 변화 없음
  - 20개 초과 : 가장 최근 목록부터 20개

### - account.dart

- 사용자의 프로필을 담아낼 레이아웃 구현
- 현재는 userid만 구현
- 추가적인 부분들은 회원가입시 입력하는 칸을 생성하여 받아올 필요 있음

