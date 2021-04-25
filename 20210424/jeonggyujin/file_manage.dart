import 'dart:convert';
import 'dart:ffi';
import 'dart:io';
import 'dart:typed_data';
import 'package:crypto/crypto.dart';
import 'package:encrypt/encrypt.dart' as encrypt;
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:path_provider/path_provider.dart';

// 입력 데이터를 해시로 출력
Future hash512(data) async {
  final bytes = utf8.encode(data); // 유니코드 변환
  final digest = sha512.convert(bytes); // 해싱
  return digest.toString(); // 문자열로 반환
}

// 사용자의 파일경로를 읽어와 반환
Future read(username) async {
  try {
    // getApplicationDocumentsDirectory() = 앱내 저장공간에 존재하는 파일들의 위치정보를 얻어오는 기능
    final dir = await getApplicationDocumentsDirectory(); //await= 비동기
    return int.parse( // int.parse() = 다른 자료형의 데이터를 int형으로 파싱하는 방법 
        // readAsString() = 전체 파일 내용을 문자열로 읽기
        // 경로/이름.txt 를 찾아서 string형태로 읽어와 int형으로 파싱 후 리턴
        await File(dir.path + '/' + username + '.txt').readAsString());
  } catch (e) { 
    print("읽기에 실패하였습니다");
    return 0;
  }
}

// 클라이언트 제네시스블록을 생성
Future genesisWrite(user_id, user_pwd, clientrandom) async {

  try {
  final dir = await getApplicationDocumentsDirectory();
  //print(dir.path);
  //
  // temp 변수에 해당하는 파일마다 id|pw|clientrandom 의 형식으로 저장
  String temp = user_id + "|" + user_pwd + "|" + clientrandom +"|";
  // final = 한번 초기화해서 지정한 변수값은 수정이 불가능함
  final new_hash = await hash512(temp); // temp를 해시하여 new_hash에 저장
  // temp 변수에 해시값을 더해 저장
  temp = temp + new_hash + "|";
  // id에 해당하는 파일에 temp값을 추가한다.
  File(dir.path + '/' + user_id + '.txt').writeAsString(temp); // writeAsString() = 파일에 데이터를 쓰는 함수
  // 값이 잘 들어갔는지 확인하는 출력
  // dir.path/user_id.txt
  // user_id|user_pwd|clientrandom|temp|
  print(await File(dir.path + '/' + user_id + '.txt').readAsString());
  return 0;
  } catch (e) {
    print("쓰기에 실패하였습니다");
    return 0;
  }
}

// 클라이언트 블록 추가
Future nextblockWrite_client(id, pwd, postcode) async {

  final dir = await getApplicationDocumentsDirectory();
  print(dir.path);
  // readAsLines() = 각 라인을 구분하여 읽는 기능. 파이썬 f.readlines()와 같은 역할수행
  final prev = await File(dir.path + '/' + id + '.txt').readAsLines();
  final data = prev.last; // prev의 마지막 라인 id|pw|postcode|new_hash| 을 data변수에 넣는다.
  final new_hash = await hash512(data); 
  File(dir.path + '/' + id + '.txt')
      // dir.path/id.txt
      // \n id|pwd|postcode|new_hash
      // id에 해당하는 파일에 개행 후 해당 id, pwd, postcode, new_hash 저장
      .writeAsString(await File(dir.path + '/' + id + '.txt').readAsString() + "\n" + id + "|" + pwd + "|" + postcode + "|"+ new_hash);
  return 0;
  
}

// 서버에 전달할 블록 생성
Future nextblockWrite_server(id, decrypted) async {

  final dir = await getApplicationDocumentsDirectory();
  final prev = await File(dir.path + '/' + id + '.txt').readAsLines();
  File(dir.path + '/' + id + '.txt').writeAsString(await File(dir.path + '/' + id + '.txt').readAsString() + "\n" + decrypted); // 개행 후 decrypted 저장

  // 정상적으로 데이터가 들어갔는지 확인
  final test = await File(dir.path + '/' + id + '.txt').readAsLines();
  print(test);
  return 0;

}

// 암호화
Future encrypting(userid, userpwd, postcode) async {
  
  print("암호화 시작 ----------------------");
  final dir = await getApplicationDocumentsDirectory();
  final prev = await File(dir.path + '/' + userid + '.txt').readAsLines();
  final lastdata = prev.last; // user 파일의 마지막라인을 lastdata에 저장= id|pw|postcode|new_hash|
  final lasthash = lastdata.split("|")[3].substring(0,32); // | 제거하고 [3] = newhash. new_hash를 32자리까지만 추출해서 lasthash에 저장
  final key = encrypt.Key.fromUtf8(lasthash); // 해시값을 인코딩후 키로 암호화
  print("암호화할 키값 : " + key.base64); // 키 base64인코딩해서 프린트

  final String data = userid + "|" + userpwd + "|" + postcode + "|";

  try {
    // 데이터를 보내기전에 암호화하는 과정

    // 해시 -> 키를 이용해 암호화
    // 키 -> 대칭키(fernet)암호화 -> encrypt암호화 -> 암호화된키를 이용한 data 암호화 -> 보낼 데이터 완성

    final fernet = encrypt.Fernet(key); // 키를 대칭키암호화해서 fernet변수에 넣음
    final encrypter = encrypt.Encrypter(fernet); // fernet변수를 암호화
    final encrypted = encrypter.encrypt(data); // fernet을 암호화한값으로 data를 암호화해서 encrypted 변수에 저장
    print("보낼 데이터 : " + encrypted.base64);
    return encrypted.base64;

  } catch(e) {

    print("???");

  }
  
}

//복호화. 키 나누고 데이터 복호화하는 부분이 완벽하게 이해안됨.
decrypting(id, response) async {

  print("복호화 시작 ---------------------");
  print("받은 암호문 : " + response.toString());
  // toString() = response 정보를 문자열로 출력
  // replaceAll() = toString을 통해 문자열에 \"이생기게되는데 이걸 지워주는 기능
  final data = response.toString().replaceAll("\"", "");
  // 받은 data를 복호화하고 base64인코딩
  final encrypt.Encrypted encrypted = encrypt.Encrypted.fromBase64(data); // data를 복호화하고 base64인코딩 후 encrypted 변수에 저장

  //final encrypt.Encrypted data = encrypt.Encrypted.fromBase64(response);
  //final encrypt.Encrypted encrypted = encrypt.Encrypted(utf8.encode(temp));

  final dir = await getApplicationDocumentsDirectory();
  final prev = await File(dir.path + '/' + id + '.txt').readAsLines();
  final prev_hash = prev.last.split("|")[3].substring(0,32); // id|pw|postcode|new_hash|
  print("복호화할 해시 : " + prev_hash);
  final d_key = encrypt.Key.fromUtf8(prev_hash); //해시를 복호화해서 암호화되어있는 키를 추출. 데이터와 암호화된키를 분리하는 작업
  print("복호화할 키값 : " + d_key.base64);

  final fernet = encrypt.Fernet(d_key); // d_key를 대칭키암호화 -> fernet
  final encrypter = encrypt.Encrypter(fernet); // fernet변수 암호화 -> encrypted
  final String decrypted = encrypter.decrypt(encrypted); // encrypted복호화후 decrypted에 문자열로 저장
  print("복호화된 데이터 : " + decrypted);

  nextblockWrite_server(id, decrypted); // 다음블록 생성하는 함수
  return decrypted;

}