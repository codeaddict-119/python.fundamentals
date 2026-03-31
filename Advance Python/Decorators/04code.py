from functools import wraps
import time

def log_and_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        print(f"{func.__name__} returned: {result}")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        
        return result
    return wrapper
