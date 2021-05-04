import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue
      ),
      home: MyHomePage(),
    );
  }
}class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        alignment: Alignment.centerLeft,
        // child: Row(
        //   mainAxisAlignment: MainAxisAlignment.center,
        //   mainAxisSize: MainAxisSize.max,
        //   crossAxisAlignment: CrossAxisAlignment.baseline,
        //   textBaseline: TextBaseline.alphabetic,
        //   //textBaseline: TextBaseline.ideographic,
        //   children: <Widget>[
        //     // Flexible = 가능한 공간에 차지할수있는 비율
        //     //Flexible(child: YellowBox(), fit: FlexFit.tight,),
        //     //Flexible(child: TallerYellowBox(), fit: FlexFit.loose,),
        //     // Flexible과 Expanded는 tihgt상태에서는 같은 기능을 함
        //     //Expanded(child: YellowBox()),
        //     //SizeBox와 Spacer는 둘다 위젯들 사이에 공간을 만들어주는건데 space는 비율, sizedbox는 정확한 사이즈 값을 사용
        //     //SizedBox(child: YellowBox(), height: 200, width: 150,),
        //     //SizedBox(height: 30,),
        //     //Spacer(flex: 1,),
        //     //TallerYellowBox(),
        //     //Spacer(flex: 5,),
        //     //YellowBox(),
        //     Text("Hey",style: TextStyle(color: Colors.yellow, fontSize: 26),),
        //     Text("Hey",style: TextStyle(color: Colors.red, fontSize: 56),),
        //     //Text("한글",style: TextStyle(color: Colors.green, fontSize: 36),),
        //     Icon(
        //       Icons.ac_unit,
        //       size: 60,
        //       color: Colors.lightBlue,
        //     ),
        //   ],
        // ),
        child: Image.network('https://i.picsum.photos/id/419/200/300.jpg?hmac=jvSs1zyCZ3ATdTlvdfcTKBBGcrgnCk3EAvZt352Fbco'),
      ),

    );
  }
}
class YellowBox extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 50,
      width: 50,
      decoration: BoxDecoration(
        color: Colors.yellowAccent,
        border: Border.all(),
      ),
    );
  }
}

class TallerYellowBox extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 50,
      width: 100,
      decoration: BoxDecoration(
        color: Colors.yellowAccent,
        border: Border.all(),
      ),
    );
  }
}


