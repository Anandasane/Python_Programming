# Python Programming

A comprehensive workspace for Python programming projects, scripts, and learning resources. This repository serves as a central hub for Python development with best practices, examples, and reusable components.

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running Python Scripts](#running-python-scripts)
- [Virtual Environment Setup](#virtual-environment-setup)
- [Core Python Concepts](#core-python-concepts)
- [Best Practices](#best-practices)
- [Testing](#testing)
- [Common Workflows](#common-workflows)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project provides:

- **Modular code organization** with clear separation of concerns
- **Reusable utilities** and helper functions
- **Example scripts** demonstrating Python best practices
- **Jupyter notebooks** for data exploration and prototyping
- **Unit tests** ensuring code reliability
- **Documentation** and code comments for maintainability

Whether you're building web applications, data pipelines, automation scripts, or learning Python, this workspace provides a solid foundation.

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

| Requirement | Version | Download Link |
|-------------|---------|---------------|
| Python | 3.8+ | [python.org](https://www.python.org/downloads/) |
| pip | Latest | Included with Python 3.4+ |
| Git | Latest | [git-scm.com](https://git-scm.com/downloads) |

**Verify your installation:**

```bash
# Check Python version
python --version

# Check pip version
pip --version

# Check Git version
git --version
```

---

## Project Structure

```
Python_Programming/
├── 📁 src/                    # Source code modules
│   ├── __init__.py
│   ├── main.py               # Application entry point
│   ├── utils/                # Utility functions and helpers
│   └── modules/              # Feature-specific modules
│
├── 📁 tests/                  # Unit and integration tests
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils/
│
├── 📁 scripts/                # Standalone utility scripts
│   ├── setup.py
│   └── automation/
│
├── 📁 data/                   # Data files and datasets
│   ├── raw/                  # Original, immutable data
│   ├── processed/            # Cleaned and transformed data
│   └── outputs/              # Generated results
│
├── 📁 notebooks/              # Jupyter notebooks for exploration
│   ├── exploratory/
│   └── prototypes/
│
├── 📁 docs/                   # Additional documentation
│   ├── architecture.md
│   └── api_reference.md
│
├── 📁 config/                 # Configuration files
│   ├── settings.py
│   └── logging.conf
│
├── .gitignore                 # Git ignore patterns
├── requirements.txt           # Python dependencies
├── requirements-dev.txt       # Development dependencies
├── setup.py                   # Package installation config
├── pyproject.toml            # Modern Python project config
└── README.md                  # This file
```

---

## Installation

### Clone the Repository

```bash
# Clone using HTTPS
git clone https://github.com/your-username/Python_Programming.git

# Or clone using SSH
git clone git@github.com:your-username/Python_Programming.git

# Navigate into the directory
cd Python_Programming
```

### Install Dependencies

```bash
# Install production dependencies
pip install -r requirements.txt

# Install development dependencies (includes testing, linting tools)
pip install -r requirements-dev.txt

# Or install the package in editable mode
pip install -e .
```

### Common Dependencies

| Package | Purpose | Install Command |
|---------|---------|---------------|
| requests | HTTP library | `pip install requests` |
| pandas | Data manipulation | `pip install pandas` |
| numpy | Numerical computing | `pip install numpy` |
| pytest | Testing framework | `pip install pytest` |
| black | Code formatter | `pip install black` |
| flake8 | Code linter | `pip install flake8` |

---

## Running Python Scripts

### Basic Execution

```bash
# Run a specific script
python src/main.py

# Run with arguments
python src/main.py --input data/raw/input.csv --output data/outputs/

# Run in verbose mode
python src/main.py -v --debug
```

### Running Modules

```bash
# Run as a module (recommended for package imports)
python -m src.main

# Run specific module functions
python -m src.utils.helpers
```

### Common Execution Patterns

```bash
# Interactive Python shell
python

# Execute a command directly
python -c "print('Hello, Python!)"

# Run a script and measure execution time
time python src/main.py

# Profile script performance
python -m cProfile src/main.py
```

---

## Virtual Environment Setup

Using virtual environments is **strongly recommended** to isolate project dependencies.

### Creating a Virtual Environment

```bash
# Using venv (built-in)
python -m venv venv

# Using virtualenv (if installed)
virtualenv venv

# Using conda
conda create -n python_env python=3.11
```

### Activating the Environment

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### Deactivating

```bash
deactivate
```

### Installing Dependencies in Virtual Environment

```bash
# Activate first, then install
source venv/bin/activate  # or Windows equivalent
pip install -r requirements.txt
```

---

## Core Python Concepts

### Variables and Data Types

```python
# Primitive types
name: str = "Python"
version: float = 3.11
is_active: bool = True

# Collections
numbers: list[int] = [1, 2, 3, 4, 5]
unique_items: set[str] = {"a", "b", "c"}
person: dict[str, str] = {"name": "Alice", "role": "Developer"}
coordinates: tuple[float, float] = (10.5, 20.3)
```

### Functions and Classes

```python
# Function with type hints
def greet(name: str, greeting: str = "Hello") -> str:
    """Return a personalized greeting."""
    return f"{greeting}, {name}!"

# Class definition
class Calculator:
    """Simple calculator class."""
    
    def __init__(self) -> None:
        self.history: list[str] = []
    
    def add(self, a: float, b: float) -> float:
        result = a + b
        self.history.append(f"Added {a} + {b} = {result}")
        return result
```

### Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Cleanup code here")
```

### Working with Files

```python
# Reading files
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Writing files
data = ["Line 1", "Line 2", "Line 3"]
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(data))

# Working with CSV
import csv
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

---

## Best Practices

### Code Style

Follow **PEP 8** guidelines for clean, readable code:

```python
# ✅ Good: Clear variable names, proper spacing
def calculate_total_price(items, tax_rate=0.08):
    subtotal = sum(item.price for item in items)
    tax_amount = subtotal * tax_rate
    return subtotal + tax_amount

# ❌ Avoid: Unclear names, poor formatting
def calc(items,t=0.08):
    s=sum([i.p for i in items])
    return s+s*t
```

### Type Hints

Use type hints for better code clarity and IDE support:

```python
from typing import List, Dict, Optional

def process_users(users: List[Dict[str, str]]) -> Optional[Dict]:
    if not users:
        return None
    return users[0]
```

### Docstrings

Document functions and classes with docstrings:

```python
def send_email(recipient: str, subject: str, body: str) -> bool:
    """
    Send an email to the specified recipient.
    
    Args:
        recipient: Email address of the recipient.
        subject: Subject line of the email.
        body: Body content of the email.
    
    Returns:
        True if email was sent successfully, False otherwise.
    
    Example:
        >>> send_email("user@example.com", "Hello", "Test message")
        True
    """
    # Implementation here
    pass
```

### List Comprehensions

Use comprehensions for clean, efficient data transformation:

```python
# ✅ Good: List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]

# ❌ Avoid: Verbose loop
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)
```

---

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_main.py

# Run with coverage report
pytest --cov=src --cov-report=html
```

### Writing Tests

```python
import pytest
from src.calculator import Calculator

class TestCalculator:
    """Test cases for Calculator class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        result = self.calc.add(2, 3)
        assert result == 5
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        result = self.calc.add(-1, -1)
        assert result == -2
    
    def test_add_zero(self):
        """Test addition with zero."""
        result = self.calc.add(5, 0)
        assert result == 5
```

---

## Common Workflows

### Adding a New Feature

1. **Create a feature branch:**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Implement the feature** in the `src/` directory

3. **Write tests** in the `tests/` directory

4. **Run tests to ensure nothing breaks:**
   ```bash
   pytest
   ```

5. **Format and lint your code:**
   ```bash
   black src/ tests/
   flake8 src/ tests/
   ```

6. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add new feature: description"
   git push origin feature/new-feature
   ```

### Data Processing Pipeline

```bash
# 1. Prepare raw data
python scripts/preprocess_data.py --input data/raw/ --output data/processed/

# 2. Run analysis
python src/analysis.py --data data/processed/dataset.csv

# 3. Generate reports
python scripts/generate_report.py --results data/outputs/
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure virtual environment is activated and dependencies are installed |
| `Permission denied` | Run terminal as administrator or use `sudo` (Linux/Mac) |
| `Port already in use` | Find and kill the process: `lsof -i :8000` then `kill -9 <PID>` |
| `Python version mismatch` | Use pyenv or specify exact Python version in virtual environment |
| `Package conflicts` | Create fresh virtual environment and reinstall dependencies |

### Debugging Tips

```python
# Use the built-in debugger
import pdb; pdb.set_trace()

# Or use Python 3.7+ breakpoint()
breakpoint()

# Log effectively
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Debug information: %s", variable)
```

---

## Resources

### Learning Python

- [Official Python Documentation](https://docs.python.org/3/)
- [Python Cookbook](https://diveintopython3.problemsolving.io/)
- [Real Python Tutorials](https://realpython.com/)
- [Python for Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

### Development Tools

- **IDEs:** VS Code, PyCharm, JupyterLab
- **Formatters:** Black, autopep8, yapf
- **Linters:** flake8, pylint, mypy
- **Testing:** pytest, unittest, coverage.py

### Package Management

- [PyPI - Python Package Index](https://pypi.org/)
- [pip documentation](https://pip.pypa.io/en/stable/)
- [conda documentation](https://docs.conda.io/en/latest/)

---

## Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork** the repository
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes** with clear, documented code
4. **Add tests** for new functionality
5. **Ensure all tests pass** (`pytest`)
6. **Format your code** (`black src/ tests/`)
7. **Commit** with descriptive messages (`git commit -m 'Add amazing feature'`)
8. **Push** to your fork (`git push origin feature/amazing-feature`)
9. **Open a Pull Request** with detailed description

### Code Review Checklist

- [ ] Code follows PEP 8 style guidelines
- [ ] Type hints are used where appropriate
- [ ] Functions and classes have docstrings
- [ ] Tests cover new functionality
- [ ] All tests pass locally
- [ ] Documentation is updated if needed

---

## License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 Python Programming Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Support

If you encounter issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Search existing [Issues](https://github.com/your-username/Python_Programming/issues)
3. Create a new issue with detailed description and steps to reproduce

---

**Happy Coding! 🐍✨**

