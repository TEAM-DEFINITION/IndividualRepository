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
  MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}
class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    /*
    var titleSection;
    var buttonSection;
    var textSection;
    */
    return Scaffold(
      body: Column(
        children: <Widget>[
          Image.network("https://www.dailysecu.com/news/photo/201809/38334_30902_5027.jpg",
              height: 400, width: 600, fit: BoxFit.cover),
          /*
          titleSection,
          buttonSection,
          textSection
          */
        ],
      )
    );
  }
}
