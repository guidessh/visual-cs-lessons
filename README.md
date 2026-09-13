# Visual Computer Science Lessons

Runnable companion code for beginner-friendly animated computer science videos.
Each video maps to one self-contained lesson folder, so you can download only
the topic you need before an interview or clone the complete collection.

## Repository map

```text
lessons/
├── data-structures/       Hash tables, linked lists, stacks, queues, trees
├── algorithms/            Searching, sorting, traversal, pathfinding
├── computer-systems/      Memory, CPUs, networking, databases
└── programming-concepts/  Language and software-development fundamentals
```

## Available lessons

### Data structures

- [Hash Tables for Beginners in Python](lessons/data-structures/hash-tables-python/README.md)

## Run everything

The lessons use the Python standard library and require no package installation.

```bash
python run_all_tests.py
```

## Lesson contract

Every lesson folder must remain independently runnable and contain:

- a `README.md` that explains the concept and commands;
- the complete source shown in the video;
- executable tests; and
- no dependency on files from another lesson folder.

See [CONTRIBUTING.md](CONTRIBUTING.md) before adding another lesson.
