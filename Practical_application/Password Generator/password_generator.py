import random
stri="1234567890!@#$%^&*()-_=+qwertyuiop[]}\|asdfghjkl:'zxcvbnm<>?,./QWERTYUIOPASDFGHJKLZXCVBNM'"
#above in stri string ,it contain all valid characters 
# It will generate a strong password
while True:
       try:
              a=input("password of what [for mail,facebook,bank etc]:")
              a1=str(a)
              lenght=int(input("Enter lenght of the password:"))
              password=""
              for a in range(lenght):
                     password+=random.choice(stri)
              print(password)
              with open("data.txt", "a") as file:
                file.write(f"{a1} password is :{password}\n")
                
              print(f" Generated and saved: {password}")
              print(f"Stored in data.txt")

            

       except ValueError:
              print("Invalid Input!!")