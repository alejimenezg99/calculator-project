

## 1. Function to ask the user for a number.
def number():
    """
    Ask the user for a number.
    If will keep asking the user for a valid number until it provides one.
    """
    while True:
        try:
            number = float(input())
            return (number)
        except ValueError:
            print("Invalid input, please enter a rational number in #.#0 format")

## 2. Function to sum 2 numbers.
def sum(verbose = True):
    """Adding a and b together."""
    print("Welcome to the addition function. Please enter the first number:")
    a = number()
    print("Thank you. Now enter the second number:")
    b = number()
    if verbose:
        print("The result of the addition between", a, "and", b, "is:")
    print(a+b)

## 3. Function to substract 2 numbers.
def substract(verbose = True):
    """Substracting b from a"""
    print("Welcome to the substraction function. Please enter the first number:")
    a = number()
    print("Thank you. Now enter the second number:")
    b = number()
    if verbose:
        print("The result of substracting", b, "from", a, "is:")
    print(a-b)

## 4. Function to multiply 2 numbers.
def multiply(verbose = True):
    """Multiplying a times b"""
    print("Welcome to the multiplying function. Please enter the first number:")
    a = number()
    print("Thank you. Now enter the second number:")
    b = number()
    if verbose:
        print("The result of multiplying", a, "times", b, "is:")
    print(a*b)

## 5. Function to divide 2 numbers.
def divide(verbose = True):
    """
    Dividing a into b.
    User must provide a value for b other than 0.
    The function will ask for a new valid number
    """
    print("Welcome to the dividing function. Please enter the first number (dividend):")
    a = number()
    print("Thank you. Now enter the second number (divisor):")
    b = number()
    while True:
        if b != 0:
            if verbose:
                print("The result of dividing", a, "into", b, "is:")
            print(a/b)
            break
        else:
            print("You cannot divide by 0. Please enter a new number")
            b = number()

## Main Function: Calculator application with menu.
def main_function(verbose = True):
    print("Welcome to Alejo's Calculator!")
    print("Please type the number corresponding to one of the following operations to perform between 2 numbers:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    list = [1, 2, 3, 4, 5]
    operation = int(input())

    while True:
        if operation in list:
            if operation == 1:
                sum(verbose)
                break
            elif operation == 2:
                substract(verbose)
                break
            elif operation == 3:
                multiply(verbose)
                break
            elif operation == 4:
                divide(verbose)
                break
            else:
                print("Thank you for visiting Alejo's calculator! Bye!")
                break
        else:
            print("Not a valid number. Please type a number between 1 and 6, each corresponding to an operation.")
            operation = int(input())

## Run the main function of the calculator app.
if __name__ == "__main__":
    main_function()