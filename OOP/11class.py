import math
class Calculator:
    def __init__(self, n):
        self.n = n
             
    def factorial(self, n=None):
        # If no n is provided, use the initial self.n
        if n is None:
            n = self.n
        if n == 1 or n == 0:
            return 1
        else:
            # Call the method again with the decremented value
            return n * self.factorial(n - 1)
        
    def squareroot(self, n=None):
        # Use n if provided, otherwise use self.n
        val = n if n is not None else self.n
        result = math.sqrt(val)
        # Return a formatted string
        return f"{result:.2f}"
    
    def table_number(self,n=None): 
        val = n if n is not None else self.n
        table=""
        for i in range(1,11):
             table+=f"{val} X {i}={val*i}\n"
        return table
    
    def sin_cos_tan(self, n=None):
        val = n if n is not None else self.n
        # Returning a tuple is the cleanest way
        return math.sin(val), math.cos(val), math.tan(val)

              
num1 = Calculator(23)
print(f"The factorial of 23={num1.factorial()}")
print(f"The square root of 23={num1.squareroot()}")
print(num1.table_number())
print(num1.sin_cos_tan())


num2=Calculator(234)
print(f"The factorial of 234={num2.factorial()}")
print(f"The square root of 234={num2.squareroot()}")
print(num2.table_number())
print(num2.sin_cos_tan())

num3=Calculator(99)
print(f"The factorial of 234={num3.factorial()}")
print(f"The square root of 234={num3.squareroot()}")
print(num3.table_number())
print(num3.sin_cos_tan())

num4=Calculator(95)
print(f"The factorial of 234={num4.factorial()}")
print(f"The square root of 234={num4.squareroot()}")
print(num4.table_number())
print(num4.sin_cos_tan())

num5=Calculator(98)
print(f"The factorial of 234={num5.factorial()}")
print(f"The square root of 234={num5.squareroot()}")
print(num5.table_number())
print(num5.sin_cos_tan())