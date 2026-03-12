import math
class calculator:
       def __init__(self,n):
              self.n=n
       def square(self):
              print(f"The square of number={self.n*self.n}")
       def cube(self):
              print(f"The cube of number={self.n*self.n*self.n}")
       def square_root(self):
              print(f"The square root of the number={math.sqrt(self.n)}")
@ staticmethod # for now it is 
def factorial(n):
       if n==1 or n==0:
              return 1
       else:
              return n*factorial(n-1)
n=int(input(">>>"))
print(f"The staticmetod work,output {factorial(n)}")
try:
       userint=int(input(">>>"))
except ValueError:
       print("Invalid Input!!")
a=calculator(userint)
a.square()
a.cube()
a.square_root()
       

