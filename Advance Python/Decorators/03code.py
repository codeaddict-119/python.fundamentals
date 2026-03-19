def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"Returned: {result}")
        print("-" * 30)
        
        return result
    return wrapper
