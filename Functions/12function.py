def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    
    total = sum(numbers)
    average = total / len(numbers)
    return average
nums = [10, 20, 30, 40]
result = calculate_average(nums)
print("Average:", result)