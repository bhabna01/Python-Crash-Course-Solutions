glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    "array": "Fixed-size sequential collection of same-type elements.",
    "variable":" Named storage for modifiable data.",
    "syntax":" Rules for code structure.",
    "compile":" Convert source code to executable code.",
   " debug": "Find and fix code errors.",
    "function": "Reusable code block performing a task."
    }

for key,value in glossary.items():
    print(f"\n{key.title()} : {value}")