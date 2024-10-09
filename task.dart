import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
            seedColor: const Color.fromARGB(255, 76, 175, 162)),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Task'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String title = '';
  void _addTask(String title) {
    setState(() {
      tasks.add(
          TaskItem(title: title, index: tasks.length, deleteFunc: _deleteTask));
    });
  }

  void _deleteTask(int index) {
    setState(() {
      tasks.removeAt(index);
    });
  }

  List<TaskItem> tasks = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Expanded(
              flex: 1,
              child: (tasks.isNotEmpty)
                  ? ListView.separated(
                      separatorBuilder: (context, index) => const Divider(
                        height: 1,
                        thickness: 1,
                        color: Color.fromARGB(237, 212, 237, 250),
                      ),
                      itemBuilder: (context, index) => tasks[index],
                      itemCount: tasks.length,
                    )
                  : const Empty(),
            ),
            Container(
              padding: const EdgeInsets.all(5),
              child: TextField(
                onSubmitted: (String text) {
                  _addTask(text);
                  setState(() {
                    title = '';
                  });
                },
                controller: TextEditingController(text: title),
                decoration: const InputDecoration(
                    border: OutlineInputBorder(), hintText: "Enter your Task"),
              ),
            )
          ],
        ),
      ),
    );
  }
}

// Widget for task view item
class TaskItem extends StatefulWidget {
  const TaskItem(
      {super.key,
      required this.title,
      required this.index,
      required this.deleteFunc});
  final int index;
  final Function deleteFunc;
  final String title;
  // ignore: empty_constructor_bodiess
  @override
  State<TaskItem> createState() => _TaskItemState();
}

class _TaskItemState extends State<TaskItem> {
  bool pending = true;

  void handleTaskCompletion() {
    Future.delayed(const Duration(seconds: 5), () {
      if (!pending) {
        widget.deleteFunc(widget.index);
        setState(() {
          pending = true;
        });
        ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
          content: Text('Task Completed'),
          duration: Duration(seconds: 1),
        ));
      }
    });
  }

  void handleTaskDeletion() {
    setState(() {
      pending = true;
    });
    ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
      content: Text('Task Deleted'),
      duration: Duration(seconds: 1),
    ));
    widget.deleteFunc(widget.index);
  }

  @override
  Widget build(BuildContext context) {
    return Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
      const SizedBox(width: 10),
      Padding(
        padding: const EdgeInsets.fromLTRB(0, 5, 0, 0),
        child: GestureDetector(
          onTap: () {
            setState(() {
              pending = !pending;
            });
          },
          child: (pending)
              ? const Icon(
                  Icons.circle_outlined,
                  color: Color.fromARGB(255, 41, 189, 144),
                  size: 25,
                )
              : const Icon(Icons.check_circle,
                  color: Color.fromARGB(255, 41, 189, 144), size: 25),
        ),
      ),
      const SizedBox(width: 10),
      Flexible(
          flex: 1,
          fit: FlexFit.tight,
          child: Text(widget.title,
              maxLines: 5,
              softWrap: true, // Added this line for line breaks
              overflow:
                  TextOverflow.visible, // Changed from ellipsis to visible
              style: TextStyle(
                fontSize: 25,
                decoration: (pending)
                    ? TextDecoration.none
                    : TextDecoration.lineThrough,
                color: (pending) ? Colors.black : Colors.grey,
              ))),
      Padding(
        padding: const EdgeInsets.fromLTRB(0, 5, 5, 0),
        child: GestureDetector(
            onTap: () {
              handleTaskDeletion();
            },
            child: const Icon(
              Icons.remove_circle_outline,
              color: Colors.red,
              size: 30,
            )),
      ),
    ]);
  }
}

class Empty extends StatelessWidget {
  const Empty({super.key});
  @override
  Widget build(BuildContext context) {
    return const Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [Text("No Tasks Pending")],
    );
  }
}