def handle_add(x, y):
    return x + y

def handle_sub(x, y):
    return x - y

def handle_mul(x, y):
    return x * y


def calculate(op, x, y):
    match op:
        case "add":
            return handle_add(x, y)
        case "sub":
            return handle_sub(x, y)
        case "mul":
            return handle_mul(x, y)
        case _:
            raise ValueError("Unsupported operation")

# Usage
print(calculate("add", 5, 3))  # 8
print(calculate("mul", 4, 2))  # 8