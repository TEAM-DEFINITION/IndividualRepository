import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);
  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    var titleSection = Row(children: <Widget>[
      Padding(padding: EdgeInsets.all(10.0)),
      Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Text('Oeschinen Lake CampGround',
              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 26)),
          Text('Kangresteg, Switzerland',
              style: TextStyle(color: Colors.grey, fontSize: 26))
        ],
      ),
      Icon(
        Icons.star,
        size: 25,
        color: Colors.amber,
      ),
      Text('41')
    ]);

    var buttonSection =
        Row(mainAxisAlignment: MainAxisAlignment.center, children: <Widget>[
      Column(children: <Widget>[
        Icon(
          Icons.call,
          size: 45,
          color: Colors.lightBlue,
        ),
        Text('CALL',
            style: TextStyle(
              color: Colors.lightBlue,
            ))
      ]),
      Padding(padding: EdgeInsets.all(30.0)),
      Column(children: <Widget>[
        Icon(
          Icons.near_me,
          size: 45,
          color: Colors.lightBlue,
        ),
        Text('ROUTE',
            style: TextStyle(
              color: Colors.lightBlue,
            ))
      ]),
      Padding(padding: EdgeInsets.all(30.0)),
      Column(children: <Widget>[
        Icon(
          Icons.share,
          size: 45,
          color: Colors.lightBlue,
        ),
        Text('SHARE',
            style: TextStyle(
              color: Colors.lightBlue,
            ))
      ])
    ]);
    var textSection = Container(
      child: Text(
          'Where there is a will there is a way.'
              'Think of the end before you begin. Carpe Diem!(Seize the day!) boys, be ambitious!!',
          style: TextStyle(fontSize: 20)),
      padding: EdgeInsets.all(40.0)
    );
    return Scaffold(
        body: Column(children: <Widget>[
      Image.network(
          'https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile7.uf.tistory.com%2Fimage%2F24283C3858F778CA2EFABE',
          height: 240,
          width: 600,
          fit: BoxFit.cover),
      Padding(padding: EdgeInsets.all(15.0)),
      titleSection,
      Padding(padding: EdgeInsets.all(15.0)),
      buttonSection,
      Padding(padding: EdgeInsets.all(15.0)),
      textSection
    ]));
  }
}
