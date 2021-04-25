import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:hybrid_access_app/signup_page.dart';
import 'dart:convert';

import 'package:hybrid_access_app/tab_page.dart';
import 'file_manage.dart' as file;

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {

  final TextEditingController _controller = TextEditingController(); // _controller = id 입력값
  final TextEditingController _controller2 = TextEditingController(); // _controller2 = pw 입력값
  List data = [];
  bool isLoading = false; // default 비활성화

  _fetchid() async { //?
    setState(() {
      isLoading = true; //활성화
    });
    // 웹서버 /app/login에 포스트메세지를 보내는데, 바디부분에 id와 pw를 보내고 수신되는 http코드를 response변수에 저장한다.
    final response = await http.post(
      Uri.parse("http://112.156.0.196:55555/app/login"),
      headers: <String, String> {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: <String, String>{
        'user_id' : _controller.text,
        'user_pwd' : _controller2.text,
      }
      ,
    );
    // 상태코드 200일때
    if(response.statusCode == 200){
      isLoading = false; // 
      // 상태코드 200 을 받으면 로그인성공 호출
      if (response.body == "200") {
        // 네비게이터 = 화면이동
        Navigator.push(context, MaterialPageRoute(builder: (context) =>
        // 탭 메시지에 로그인성공메세지와함께, 입력한 id, id, pw 출력
        TabPage(data:"로그인성공\n 이름 : "+_controller.text,
                userid: _controller.text, 
                userPwd: _controller2.text,
        )));
      // 서버로부터 401을 받음
      } else if (response.body == "401") {

        _showDialogLoginIdFail();
        _controller.text = ""; // 입력한 id를 초기화. 없애주는 것
        _controller2.text = ""; // 입력한 pw를 없애주는 것
      // 서버로부터 402를 받음
      } else if (response.body == "402") {

        _showDialogLoginPwdFail();
        _controller.text = "";
        _controller2.text = "";

      }
      
    } else{
      throw Exception("failed to load data");

    }
  }

  // 401 Unauthorized
  // 아이디 불일치시 호출되는 함수
  void _showDialogLoginIdFail() {
    showDialog(//alert메세지 출력
      context: context,
      builder: (BuildContext context) {
        // return object of type Dialog
        return AlertDialog(
          title: new Text("로그인 실패"),
          content: new Text("아이디가 존재하지 않습니다!!"),
          actions: <Widget>[
            new FlatButton(
              child: new Text("닫기"),
              onPressed: () {
                Navigator.pop(context); // 닫기버튼누르면 화면에서빠져나옴
              },
            ),
          ],
        );
      },
    );
    _controller.text = "";
    _controller2.text = "";

  }

  // 402 Payment Required
  // 패스워드 불일치시 호출되는 함수
  void _showDialogLoginPwdFail() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        // return object of type Dialog
        return AlertDialog(
          title: new Text("로그인 실패"),
          content: new Text("비밀번호가 틀립니다!!"),
          actions: <Widget>[
            new FlatButton(
              child: new Text("닫기"),
              onPressed: () {
                Navigator.pop(context); // 닫기버튼누르면 화면에서빠져나옴
              },
            ),
          ],
        );
      },
    );
    _controller.text = "";
    _controller2.text = "";

  }

  _signup() async {

    Navigator.push(context, MaterialPageRoute(builder: (context) => SignUp()));

  }

  @override
  void dispose(){
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {

    Size screenSize = MediaQuery.of(context).size;
    double width = screenSize.width;
    double height = screenSize.height;

    return SafeArea(
      child: Scaffold(
        appBar: AppBar(
          title: Text("로그인", style: TextStyle(color: Colors.black)),
          backgroundColor: Colors.white38,
          leading: Container(),
        ),

        body:
          Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children : <Widget>[
              Center(
                child:
                  TextFormField(
                    controller: _controller,
                    autofocus: true,
                    decoration:
                      InputDecoration(
                        icon: Icon(Icons.account_circle),
                        border: InputBorder.none,
                        labelText: "이름 또는 아이디를 입력하세요",
                        counterText: ""
                      ),
                    maxLength: 10
                  ),
              ),
              Center(
                child:
                  TextFormField(
                    controller: _controller2,
                    obscureText: true,
                    autofocus: true,
                    decoration:
                      InputDecoration(
                        icon: Icon(Icons.security_rounded),
                        border: InputBorder.none,
                        labelText: "비밀번호를 입력하세요",
                        counterText: ""
                      ),
                    maxLength: 10
                  ),
              ),
              Center(
                child:
                  TextButton(
                    child:
                      Text("로그인"),
                    style:
                      TextButton.styleFrom(primary:Colors.blue),
                    onPressed: (){
                      _fetchid();
                    }
                  )
                    
              ),
              Center(
                child:
                  TextButton(
                    child:
                      Text("아직 회원이 아니신가요?"),
                    style:
                      TextButton.styleFrom(primary:Colors.grey),
                    onPressed: (){
                      _signup();
                    }
                  )
                    
              ),
            ]
          )
          
      ),
    );
  }
}
