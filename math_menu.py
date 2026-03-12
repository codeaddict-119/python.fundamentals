import math
# input like :2324.00
# don't input like :2324

while True:
    print("\n1. Area of Circle")
    print("2. Circumference of Circle")
    print("3. Area of Square")
    print("4. Surface Area of Sphere")
    print("5. Volume of Sphere")
    print("6. Terminate Process")

    ch = input("Enter your choice (1-6): ")

    if ch == '1':
        try:
            r = float(input("Enter radius of the circle: "))
            area = math.pi * r ** 2
            print(f"Area of Circle = {area}")
        except ValueError:
            print("Enter a valid number!")

    elif ch == '2':
        try:
            r = float(input("Enter radius of the circle: "))
            circumference = 2 * math.pi * r
            print(f"Circumference of Circle = {circumference}")
        except ValueError:
            print("Enter a valid number!")

    elif ch == '3':
        try:
            side = int(input("Enter the side of square: "))
            area = side ** 2
            print(f"Area of Square = {area}")
        except ValueError:
            print("Enter a valid number!")

    elif ch == '4':
        try:
            r = float(input("Enter the radius of sphere: "))
            surface_area = 4 * math.pi * r ** 2
            print(f"Surface Area of Sphere = {surface_area}")
        except ValueError:
            print("Enter a valid number!")

    elif ch == '5':
        try:
            r = float(input("Enter the radius of sphere: "))
            volume = (4/3) * math.pi * r ** 3
            print(f"Volume of Sphere = {volume}")
        except ValueError:
            print("Enter a valid number!")

    elif ch == '6':
        print("Process Terminated")
        break

    else:
        print("Invalid Choice! Please select between 1-6.")
