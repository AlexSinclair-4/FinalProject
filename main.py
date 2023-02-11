class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result = num1 + num2
        return self.result

    def subtract(self, num1, num2):
        self.result = num1 - num2
        return self.result

    def multiply(self, num1, num2):
        self.result = num1 * num2
        return self.result

    def divide(self, num1, num2):
        if num2 != 0:
            self.result = num1 / num2
            return self.result
        else:
            return "Error: Division by zero."

    def operate(self, operator, num1, num2):
        if operator == '+':
            return self.add(num1, num2)
        elif operator == '-':
            return self.subtract(num1, num2)
        elif operator == '*':
            return self.multiply(num1, num2)
        elif operator == '/':
            return self.divide(num1, num2)
        else:
            return "Error: Invalid operator."


calculator = Calculator()

print("Welcome to the calculator program.")

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    result = calculator.operate(operator, num1, num2)
    print("Result:", result)

    again = input("Do you want to calculate again? (yes/no) ")
    if again == "no":
        break

print("Exiting calculator program.")
