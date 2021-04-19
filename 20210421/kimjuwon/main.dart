import 'package:flutter/material.dart';

void main() => runApp(MyApp());
// main이 MyApp()을 호출해서 runApp한다.

// Stateless : 바뀌지 않는 정적인 것
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Juwon Demo',
      theme : ThemeData(primarySwatch:Colors.blue),
      home : MyHomePage(title : 'Juwon Demo Home Page')
    );
  }
}

// Stateful : 바꿀수 있는 것
class MyHomePage extends StatefulWidget {
  final String title;
  MyHomePage({Key key, this.title}) : super(key : key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0; //언더바가 의미하는 것은 private

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar : AppBar(title : Text(widget.title)),
      body : Center(
        child:Column(mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text('when you push, count += 3'),
          Text('$_counter', style:Theme.of(context).textTheme.display1)
        ]
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  }

  void _incrementCounter() {
    // setState : 변경사항을 저장하는 것
    setState(() {
      _counter+=3;
    });
  }
}
