## Flutter Part (signup_page)

- Choi Jinho / Baek Heewon / JI Yeongbin

### 코드 수정 내용


                Center(
                  child: TextFormField(
                      controller: _idcontroller,
                      autofocus: true,
                      // keyboardType: TextInputType.number,
                      inputFormatters: [
                        // ignore: deprecated_member_use
                        WhitelistingTextInputFormatter(RegExp('[A-Za-z0-9]'))
                      ],
                      decoration: InputDecoration(
                          icon: Icon(Icons.security_rounded),
                          border: InputBorder.none,
                          labelText: "아이디",
                          counterText: ''),
                      maxLength: 10),
                ),
                Center(
                  child: TextFormField(
                      controller: _pwdcontroller,
                      obscureText: true,
                      autofocus: true,
                      // keyboardType: TextInputType.number,
                      inputFormatters: [
                        WhitelistingTextInputFormatter(RegExp('[A-Za-z0-9]'))
                      ],
                      decoration: InputDecoration(
                          icon: Icon(Icons.security_rounded),
                          border: InputBorder.none,
                          labelText: "비밀번호",
                          counterText: ''),
                      maxLength: 10),
                ),
                Center(
                  child: TextFormField(
                    controller: _pwdcheckcontroller,
                    obscureText: true,
                    autofocus: true,
                    // keyboardType: TextInputType.number,
                    inputFormatters: [
                      WhitelistingTextInputFormatter(RegExp('[A-Za-z0-9]'))
                    ],
                    decoration: InputDecoration(
                        icon: Icon(Icons.account_circle),
                        border: InputBorder.none,
                        labelText: "비밀번호 확인",
                        counterText: ''),
                    maxLength: 10,
                  ),
                ),
                Center(
                    child: TextButton(
                        child: Text("회원가입"),
                        style: TextButton.styleFrom(primary: Colors.blue),
                        onPressed: () {
                          _fetchSignUp();
                        })),
              ])),


