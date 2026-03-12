'''This calculator has some limitations like:
1.It performs calculations step-by-step, not by mathematical precedence.
2.No Error Handling for Large Numbers[999999999999999999 ** 999999]
3.Cannot type full expression like:5 + 3 - 2
4.Floating point precision problems may occur:[input=0.1 + 0.2,output=0.30000000000000004] '''
def factorial_(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result


def calculator():

    print("Simple Calculator")
    print("Type '=' to finish current calculation")
    print("Type 'new' to start a new calculation")
    print("Type 'exit' to quit program")

    while True:  # Main program loop

        try:
            result = float(input("\nEnter first number: "))
        except ValueError:
            print("Invalid number.")
            continue

        while True:  # Current calculation loop

            operator = input("Enter operator (+, -, *, /, !) or '=': ")

            if operator == "exit":
                print("Goodbye.")
                return

            if operator == "new":
                print("Starting new calculation...")
                break

            if operator == "=":
                print("Final Result:", result)
                break

            if operator not in ["+", "-", "*", "/", "!"]:
                print("Invalid operator.")
                continue

            # FACTORIAL (Unary Operator) 
            if operator == "!":
                if result < 0 or not result.is_integer():
                    print("Factorial only works for non-negative integers.")
                    continue

                result = factorial_(int(result))
                print("Current Result:", result)
                continue

            try:
                number = float(input("Enter next number: "))
            except ValueError:
                print("Invalid number.")
                continue

            if operator == "+":
                result += number
            elif operator == "-":
                result -= number
            elif operator == "*":
                result *= number
            elif operator == "/":
                if number == 0:
                    print("Cannot divide by zero.")
                    continue
                result /= number

            print("Current Result:", result)


calculator()

