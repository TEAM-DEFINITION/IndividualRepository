## 버전 문제 해결

- minSdkVersion 수정 

  ```
  defaultConfig {
      // TODO: Specify your own unique Application ID (https://developer.android.com/studio/build/application-id.html).
      applicationId "com.example.ksjr_testing"
      minSdkVersion 18 (16 -> 18)
      targetSdkVersion 30
      versionCode flutterVersionCode.toInteger()
      versionName flutterVersionName
  }
  ```

- flutter_secure_storage 관련 간단한 예제 사용
  - 앱 재부팅 시 storage에 값이 저장, 추출되는 부분 확인
  - 비대칭키 생성 및 저장 관련 파트 진행 중

## 비대칭키 생성 (RSA)

- 키 생성 관련 api 사용법 확인 중