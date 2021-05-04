
// https://www.youtube.com/watch?v=2iWJRAcEsaQ&t=1s Flutter | 플러터 입문 강좌 - 고급 스킬 포함(Bloc, Stream)

import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart';
import 'package:friendlychat/src/random_list.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: RandomList(),
    );
  }
}