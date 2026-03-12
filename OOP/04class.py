import math

class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def divide(self, a: float, b: float):
        if b == 0:
            return "Error: Division by zero is undefined."
        return a / b

    def integer_divide(self, a: float, b: float):
        if b == 0:
            return "Error: Division by zero is undefined."
        return a // b

    def factorial(self, a: float):
        
        if a < 0 or not float(a).is_integer():
            return 
        return math.factorial(int(a))
    # Or this can be used
    '''def factorial(a):
    if a< 0:
        raise ValueError("Factorial not defined for negative numbers")
    if a == 0 or a == 1:
        return 1
    return a * factorial(a - 1)
while True:
    try:
        a= int(input(">> "))
        print(f"factorial of the number is: {factorial(a)}")
        break
    except ValueError as e:
        print("Invalid input:", e)
'''
calc = Calculator()

try:
    val_a = float(input("Enter value a: "))
    val_b = float(input("Enter value b: "))

    print(f"\nResults for {val_a} and {val_b}:")
    print(f"Addition:{calc.add(val_a, val_b)}")
    print(f"Subtraction:{calc.subtract(val_a, val_b)}")
    print(f"Division:{calc.divide(val_a, val_b)}")
    print(f"Integer Div:{calc.integer_divide(val_a, val_b)}")
    print(f"Factorial of a:{calc.factorial(val_a)}")

except ValueError:
    print("Invalid input! Please enter numeric values.")