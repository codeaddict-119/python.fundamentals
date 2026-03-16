# Arrays passing to a function that calculates 
# Arithmetic mean of the list elements

def arithmetic_mean(array):# function
    return sum(array) / len(array)# pro way 
       # length=len(array)
       # total=0
       # for i in range(length):
       #        total+=array[i]
       # return total / length
# Input list
array1=[]
try:
       limit=int(input("Enter number of elements you want :"))
       for n in range(limit):
              x=int(input("Enter the element :"))
              array1.append(x)
except ValueError:
       print("Invalid Input !!")
result= arithmetic_mean(array1)
print(array1)
print(f"Arithmetic mean of the list elements = {round(result,2)}")