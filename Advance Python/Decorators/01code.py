''' @my_decorator is syntactic sugar for say_hello = my_decorator(say_hello). 
It modifies the behavior of say_hello() by wrapping it inside wrapper(). 
The wrapper function adds behavior before and after the original function call.'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()