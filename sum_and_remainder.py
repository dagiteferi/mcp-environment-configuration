"""
Python script to read two numbers from the user, return their sum and remainder,
and provide guidance if invalid input is entered. Refactored to use a class.
"""

class NumberProcessor:
    def __init__(self):
        self.num1 = None
        self.num2 = None

    def get_number(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number (e.g., 5, 3.14). Try again.")

    def read_inputs(self):
        print("Enter two numbers to calculate their sum and remainder (first divided by second).")
        self.num1 = self.get_number("Enter the first number: ")
        self.num2 = self.get_number("Enter the second number: ")

    def calculate(self):
        total = self.num1 + self.num2
        try:
            remainder = self.num1 % self.num2
        except ZeroDivisionError:
            print("Cannot divide by zero for remainder calculation.")
            remainder = None
        return total, remainder

    def display_results(self, total, remainder):
        print(f"Sum: {total}")
        if remainder is not None:
            print(f"Remainder (first % second): {remainder}")
        else:
            print("Remainder: Undefined (division by zero)")

def main():
    processor = NumberProcessor()
    processor.read_inputs()
    total, remainder = processor.calculate()
    processor.display_results(total, remainder)

if __name__ == "__main__":
    main()
