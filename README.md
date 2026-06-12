# Python Programming Practice

A lightweight workspace for Python programs, exercises, coding challenges, and small learning projects.

## Purpose

This repository is used to:

- Practice Python syntax and problem-solving
- Build reusable examples for core programming concepts
- Store algorithm, data structure, and mini-project solutions
- Track progress as new programs are added

## Current Contents

This repository includes starter practice scripts across the `practice/` folders plus shared helpers in `utils.py`. The `basics/` folder contains common beginner programs such as HCF, GCD, LCM, prime numbers, factorials, Fibonacci series, palindrome checks, temperature conversion, and number base conversion. The `oop/` folder contains object-oriented programming concept examples.

## Program Format

Each program follows this structure:

1. Problem Statement
2. Intuition
3. Input section
4. Logic section with explanation comments
5. Output section

## Suggested Folder Structure

```text
Python_Programming/
├── practice/
│   ├── basics/           # Variables, loops, conditionals, functions
│   ├── data_structures/  # Lists, tuples, sets, dictionaries, stacks, queues
│   ├── algorithms/       # Sorting, searching, recursion, and complexity
│   ├── challenges/       # Coding challenge solutions
│   ├── mini_projects/    # Small end-to-end projects
│   └── oop/              # Object-oriented programming concepts
├── utils.py              # Reusable helper functions
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- A code editor such as VS Code, PyCharm, or any Python-friendly IDE

### Optional Virtual Environment

Creating a virtual environment is recommended when a project uses external packages.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

If `py` is not available, use:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Running a Python Script

Run a script directly with Python:

```powershell
python practice\basics\hello_world.py
```

For scripts that accept command-line arguments, pass them after the file name:

```powershell
python practice\challenges\solution.py --input sample.txt
```

## Adding a New Program

1. Create a new `.py` file in the appropriate folder.
2. Start with a problem statement and intuition comment.
3. Add an input section before the logic.
4. Add logic explanation comments for important steps.
5. End with clear output statements.
6. Run the script to verify it works.
7. Add any required dependencies to `requirements.txt` if external packages are used.

## Recommended Practices

- Keep each script focused on one idea or problem.
- Use `if __name__ == "__main__":` when a file contains reusable functions.
- Prefer standard-library modules when no external package is needed.
- Add a `requirements.txt` file when third-party packages are required.
- Avoid committing sensitive data, passwords, API keys, or private credentials.
- Update this README when a new folder, project, or setup step is added.

## Common Practice Topics

- Core Python: variables, strings, lists, tuples, sets, dictionaries
- Control flow: conditionals, loops, comprehensions
- Functions and modules
- Object-oriented programming: classes, objects, inheritance, encapsulation, polymorphism, abstraction, properties, operator overloading, composition
- File handling and exceptions
- Data structures and algorithms
- Mini projects and automation scripts
- Optional data science and machine learning experiments

## Maintenance Checklist

Before committing changes:

- [ ] The script runs without errors
- [ ] File names are descriptive
- [ ] New dependencies are documented
- [ ] No sensitive data is included
- [ ] The README is updated if the repository structure changed
