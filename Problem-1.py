class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"

# Example usage
calc = Calculator()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()

if operation == "add":
    print("Result:", calc.add(a, b))
elif operation == "subtract":
    print("Result:", calc.subtract(a, b))
elif operation == "multiply":
    print("Result:", calc.multiply(a, b))
elif operation == "divide":
    print("Result:", calc.divide(a, b))
else:
    print("Invalid operation")
