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
      body: [Home(), Abc(), Settings()][currentIndex],
      bottomNavigationBar: NavigationBar(
          destinations: [
            NavigationDestination(label: "Home", icon: Icon(Icons.home)),
            NavigationDestination(label: "Abc", icon: Icon(Icons.abc)),
            NavigationDestination(
                label: "Settings", icon: Icon(Icons.settings)),
          ],
          selectedIndex: currentIndex,
          onDestinationSelected: (int value) => {
                setState(() {
                  currentIndex = value;
                })
              }),
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
            children: [
          Text("Home Page"),
          Container(
              child: Text(
                "Search",
                style:
                    TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
              ),
              padding: EdgeInsets.all(10),
              decoration: BoxDecoration(
                  borderRadius: BorderRadius.all(Radius.circular(10)),
                  color: Colors.blue))
        ]));
  }
}

class Abc extends StatelessWidget {
  const Abc({super.key});
  @override
  Widget build(BuildContext context) {
    return Center(
        child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [Text("ABC")]));
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
