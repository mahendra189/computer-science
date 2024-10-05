import 'package:flutter/material.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatefulWidget {
  const MainApp({super.key});
  @override
  State<MainApp> createState() => _HomePage();
}

class _HomePage extends State<MainApp> {
  String wel = "Welcome to Programming";
  int currentIndex = 0;
  void updateMessage() {
    setState(() {
      wel = "Hello World!";
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
      body: Home(),
//       bottomNavigationBar: NavigationBar(
//           destinations: [
//             NavigationDestination(label: "Home", icon: Icon(Icons.home)),
//             NavigationDestination(label: "Abc", icon: Icon(Icons.abc)),
//             NavigationDestination(
//                 label: "Settings", icon: Icon(Icons.settings)),
//           ],
//           selectedIndex: currentIndex,
//           onDestinationSelected: (int value) => {
//                 setState(() {
//                   currentIndex = value;
//                 })
//               }),
    ));
  }
}

class Home extends StatelessWidget {
  const Home({super.key});
  @override
  Widget build(BuildContext context) {
    return Center(
        child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisSize: MainAxisSize.max,
            children: [
          Container(
              child: TextField(
                decoration: InputDecoration(
                    labelText: 'Search ...', contentPadding: EdgeInsets.all(5)),
              ),
              margin: EdgeInsets.all(5),
              decoration: BoxDecoration(
                  borderRadius: BorderRadius.all(Radius.circular(10)),
                  color: Colors.black12,
                  border: Border.all(
                    width: 1,
                    color: Colors.black12,
                    style: BorderStyle.solid,
                  ))),
//           Expanded(
//               child: ListView(
//             padding: EdgeInsets.all(10),
//             children: [
//               Item(value: "Hello1"),
//               Divider(),]
//             scrollDirection: Axis.vertical,
//           ))
          Expanded(
              child: ListView.builder(
            padding: EdgeInsets.all(5),
            itemCount: entries.length,
            itemBuilder: (context, index) {
              return Item(value: entries[index]);
            },
          ))
        ]));
  }
}

final List<String> entries = <String>[
  'Nimbaram',
  'Rajudevi',
  'Meena',
  'Mahendra',
  'Mahaveer',
  'Suthar',
  'macOS',
  'Sequoia',
  'Sonoma',
  'Ventura',
  'Monterey',
  'BigSur'
];

class Item extends StatefulWidget {
  const Item({super.key, required this.value});
  final String value;
  State<Item> createState() => _ItemState();
}

class _ItemState extends State<Item> {
  Color bg = Colors.black12;
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
        onTapDown: (details) => {
              setState(() {
                bg = Colors.black26;
              })
            },
        onTapUp: (details) => {
              setState(() {
                bg = Colors.black12;
              })
            },
        onTap: () {
          Navigator.push(
              context,
              MaterialPageRoute(
                  builder: (context) => Abc(param: widget.value)));
        },
        child: Container(
          child: Row(
            children: [
              Container(
                  child: Icon(Icons.mail),
                  decoration: BoxDecoration(
                    color: Colors.black12,
                    borderRadius: BorderRadius.all(Radius.circular(10)),
                  ),
                  padding: EdgeInsets.all(5)),
              SizedBox(width: 5),
              Text(widget.value)
            ],
          ),
          padding: EdgeInsets.all(5),
          margin: EdgeInsets.only(bottom: 5),
          decoration: BoxDecoration(
              color: bg,
              borderRadius: BorderRadius.all(Radius.circular(10)),
              border: Border.all(
                  width: 1,
                  color: Colors.black26,
                  strokeAlign: BorderSide.strokeAlignCenter)),
        ));
  }
}

class Abc extends StatelessWidget {
  Abc({super.key, required this.param});
  String param;
  @override
  Widget build(BuildContext context) {
    return Center(
        child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
          ElevatedButton(
            onPressed: () {
              Navigator.pop(context);
            },
            child: Icon(Icons.arrow_back_ios),
          ),
          Text(param,
              style: TextStyle(
                  fontSize: 20, color: Colors.black12, decoration: null))
        ]));
  }
}

class Settings extends StatelessWidget {
  const Settings({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
        child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [Text("Settings")]));
  }
}
