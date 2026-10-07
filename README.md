# Calculator Project

A Python calculator application with basic arithmetic operations, input validation, and robust error handling.

## Author
- **Name:** Alejandro Jimenez Gomez
- **Email:** a.jimenezg@student.ie.edu
- **Institution:** IE University
- **Date:** October 2026

## Project Overview

This calculator implements fundamental arithmetic operations with a focus on code quality, user experience, and educational value. The project demonstrates core Python programming concepts including functions, loops, exception handling, and input validation.

## Features

### Arithmetic Operations

- ➕ **Addition** - Add two numbers
- ➖ **Subtraction** - Subtract two numbers  
- ✖️ **Multiplication** - Multiply two numbers
- ➗ **Division** - Divide two numbers with zero-division protection

### Advanced Functionality

- **Input Validation:** Prevents crashes from non-numeric inputs using try-except blocks
- **Smart Error Handling:** Provides helpful, user-friendly error messages with emoji indicators
- **Type-Safe Input:** Validates all numeric inputs before processing
- **Edge Case Handling:** 
  - Division by zero detection
  - Non-numeric input rejection with helpful prompts
  - Invalid operation handling

## Project Structure

```
calculator-project/
├── .python-version          # Python version specification (if present)
├── pyproject.toml          # UV project configuration
├── README.md               # This documentation file
├── src/                    # Source directory (UV structure)
└── calculator.py           # Main calculator implementation
```

## Requirements

- Python 3.8 or higher
- UV package manager (for project initialization and management)

## Installation

This project was created using the UV package manager:

```bash
# Project was initialized with:
uv init calculator-project
```

No external dependencies are required - the calculator uses only Python standard library features.

## How to Run

1. Navigate to the project directory:
```bash
cd calculator-project
```

2. Run the calculator:
```bash
python3 calculator.py
```

## Usage Guide

### Basic Operations

When you run the calculator, you'll see:

```
========================================
       Simple Calculator
========================================
Operations:
  + : Addition
  - : Subtraction
  * : Multiplication
  / : Division

Enter first number: 
```

### Example Sessions

**Addition:**
```
Enter first number: 15
Enter operation (+, -, *, /): +
Enter second number: 7

✅ Result: 15.0 + 7.0 = 22.0
```

**Subtraction:**
```
Enter first number: 20
Enter operation (+, -, *, /): -
Enter second number: 8

✅ Result: 20.0 - 8.0 = 12.0
```

**Multiplication:**
```
Enter first number: 6
Enter operation (+, -, *, /): *
Enter second number: 7

✅ Result: 6.0 × 7.0 = 42.0
```

**Division:**
```
Enter first number: 50
Enter operation (+, -, *, /): /
Enter second number: 4

✅ Result: 50.0 ÷ 4.0 = 12.5
```

## Error Handling Examples

### Invalid Number Input

The calculator keeps asking until valid input is received:

```
Enter first number: hello
⚠️  Invalid input! Please enter a number (e.g., 5, 3.14, -2.5)
Enter first number: abc123
⚠️  Invalid input! Please enter a number (e.g., 5, 3.14, -2.5)
Enter first number: 42
```

This ensures the program never crashes from bad input!

### Division by Zero

```
Enter first number: 10
Enter operation (+, -, *, /): /
Enter second number: 0

❌ Error: Cannot divide by zero
```

### Invalid Operation

```
Enter first number: 5
Enter operation (+, -, *, /): ^

❌ Invalid operation! Please use +, -, *, or /
```

## Implementation Details

### Function Architecture

The calculator is built with modular, reusable functions:

1. **`add(a, b)`** - Returns the sum of two numbers
2. **`subtract(a, b)`** - Returns the difference between two numbers
3. **`multiply(a, b)`** - Returns the product of two numbers
4. **`divide(a, b)`** - Returns the quotient, with zero-check protection
5. **`get_number(prompt)`** - Validates and retrieves float input from user
6. **`calculator()`** - Main program flow and user interface

### Input Validation Pattern

Uses Python's try-except mechanism with while loops:

```python
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number  # Only exits on success
        except ValueError:
            print("Invalid input! Please enter a number")
            # Loop continues, asks again
```

This pattern ensures:
- No crashes from invalid input
- User receives helpful feedback
- Program continues until valid input is provided

### Division Safety

```python
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"
```

Mathematical rules are enforced to prevent runtime errors.

## Learning Objectives Demonstrated

This project showcases the following programming concepts:

✅ **Functions** - Modular design with clear single-purpose functions  
✅ **Loops** - While-loops for validation  
✅ **Conditionals** - If-elif-else chains for operation selection  
✅ **Exception Handling** - Try-except blocks for robust error management  
✅ **User Input** - input() with validation and helpful prompts  
✅ **String Formatting** - F-strings for clear output messages  
✅ **Code Organization** - Main guard pattern (`if __name__ == "__main__":`)  
✅ **Edge Cases** - Handling zero division and invalid inputs  
✅ **Documentation** - Clear comments and docstrings  

## Assignment Context

This project was created as part of a Python programming assignment for IE University, demonstrating:
- Proper project structure using UV package manager
- Version control with Git/GitHub
- Professional documentation
- Clean, readable, well-commented code
- Comprehensive error handling
- User experience design

## Testing Checklist

Before submission, the following tests were performed:

- ✅ Addition with positive numbers
- ✅ Subtraction with negative results
- ✅ Multiplication with decimals
- ✅ Division with decimal results
- ✅ Division by zero (error handling)
- ✅ Invalid number input (string instead of number)
- ✅ Invalid operation input (unsupported symbol)
- ✅ Negative numbers (-5 + 3 = -2)
- ✅ Decimal precision (3.5 * 2.5 = 8.75)

## Code Quality Features

### Readability
- Clear function names that describe their purpose
- Consistent formatting and indentation
- Helpful comments explaining logic
- Docstrings for all functions

### Reliability
- Never crashes from user input errors
- Handles mathematical edge cases (division by zero)
- Validates all inputs before processing
- Provides clear error messages

### User Experience
- Intuitive prompts guide the user
- Error messages suggest correct input format
- Clean, organized output formatting

## Future Enhancements

Potential improvements for future versions:

- 🔄 **Continuous operation mode** - Perform multiple calculations without restarting
- 📊 **Operation history** - Keep track of previous calculations
- 🔢 **Additional operations** - Exponentiation, modulo, square root
- 💾 **Save results** - Export calculation history to a file
- 🎨 **Enhanced UI** - Color-coded output, better formatting
- ⌨️ **Expression parsing** - Accept full expressions like "5 + 3 * 2"

## Technical Notes

### Python Version
Compatible with Python 3.8+. Uses standard library only.

### UV Package Manager
Project structure follows UV conventions for modern Python projects. The `pyproject.toml` file contains project metadata and is the standard for Python packaging.

### Code Style
Follows PEP 8 Python style guidelines for readability and consistency.

## Troubleshooting

**Issue:** Calculator doesn't start  
**Solution:** Ensure you're running with Python 3: `python3 calculator.py`

**Issue:** Invalid input causes crash  
**Solution:** This shouldn't happen! The code has comprehensive error handling. If it does, please report the exact input sequence.

**Issue:** Import errors  
**Solution:** No imports required - uses only Python standard library.

## Contact

For questions about this project:
- **Student:** Alejandro Jimenez Gomez
- **Email:** a.jimenezg@student.ie.edu
- **Institution:** IE University

## License

Created for educational purposes - IE University Assignment 2026

---

**Project Status:** ✅ Complete and tested  
**Last Updated:** October 7, 2026  
**Version:** 1.0.0