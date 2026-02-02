"""
A simple Python script to read two numbers from the user, return their sum and remainder,
and provide guidance if invalid input is entered.
"""

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 5, 3.14). Try again.")

def main():
    print("Enter two numbers to calculate their sum and remainder (first divided by second).")
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    
    total = num1 + num2
    try:
        remainder = num1 % num2
    except ZeroDivisionError:
        print("Cannot divide by zero for remainder calculation.")
        remainder = None
    print(f"Sum: {total}")
    if remainder is not None:
        print(f"Remainder (first % second): {remainder}")
    else:
        print("Remainder: Undefined (division by zero)")

if __name__ == "__main__":
    main()
