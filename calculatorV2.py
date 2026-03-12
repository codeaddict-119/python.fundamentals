class Calculator:

    def __init__(self):
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }

    def apply_operator(self, values, operators):
        right = values.pop()
        left = values.pop()
        operator = operators.pop()

        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            values.append(left / right)

    def evaluate(self, expression):
        values = []
        operators = []
        i = 0

        while i < len(expression):

            if expression[i] == " ":
                i += 1
                continue

            if expression[i].isdigit():
                num = ""
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                values.append(float(num))
                continue

            # If opening parenthesis
            if expression[i] == '(':
                operators.append(expression[i])

            # If closing parenthesis
            elif expression[i] == ')':
                while operators and operators[-1] != '(':
                    self.apply_operator(values, operators)
                operators.pop()  # remove '('

            # If operator
            else:
                while (operators and operators[-1] in self.precedence and
                       self.precedence[operators[-1]] >= self.precedence[expression[i]]):
                    self.apply_operator(values, operators)

                operators.append(expression[i])

            i += 1

        # Apply remaining operators
        while operators:
            self.apply_operator(values, operators)

        return values[0]


def main():
    calc = Calculator()

    print("Advanced Python Calculator")
    print("Type 'exit' to quit")

    while True:
        user_input = input("Enter expression: ")

        if user_input.lower() == "exit":
            print("Goodbye.")
            break

        try:
            result = calc.evaluate(user_input)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

       