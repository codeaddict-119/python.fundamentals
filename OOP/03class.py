class number:
       a=4
o= number()
print(o.a)# Prints the class attribute because the instance attribute is not present

o.a=0# Instance attribute given

print(o.a)# This will print Instance attribute as it is given

print(number.a)# This will print the class attribute
