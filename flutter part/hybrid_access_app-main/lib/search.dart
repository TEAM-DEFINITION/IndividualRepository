import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'file_manage.dart' as file;

List<String> entries=['null'];

class Search extends StatefulWidget {
  @override
  _SearchState createState() => _SearchState();
}

class _SearchState extends State<Search> {
  var refreshKey = GlobalKey<RefreshIndicatorState>();

  Future<Null> refreshList() async {
    refreshKey.currentState?.show(atTop: false);
    await Future.delayed(Duration(seconds: 0));
    setState(() {
      new Search();
    });
    return null;
  }

  _fetch() async{
    entries = await file.fetch();
  }
  @override
  Widget build(BuildContext context) {
    _fetch();
    return Scaffold(
        appBar: AppBar(
          title: Text('방문 기록'),
        ),
      body: RefreshIndicator(
          child: new ListView.separated(
          padding: const EdgeInsets.all(50.0),
          itemCount: entries.length, //길이만큼
          itemBuilder: (BuildContext context, int index) {
            return Container(
                padding: EdgeInsets.all(8.0), // padding
                child: Text('${entries[index]}')
            );
          },
          separatorBuilder: (BuildContext context, int index) => const Divider(),
        ),
        onRefresh: refreshList,
        key: refreshKey,
      )
    );
  }
}