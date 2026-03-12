# This a very basic snake water gun game 
# It use python random function for computer random choice
# It take user input in string form
import random
li={1:'snake',2:'water',3:'gun'}# for computer
rev={'snake':1,'water':2,'gun':3}# for user
while True:
 computer=random.randint(1,3)
 computer_choice=li[computer]
 user=input("Enter [snake,water,gun]:").lower()# Taking input
 if user not in rev:
    print("Invalid choice!!")
 else:
    if user=='snake'and computer==1 or user=='water'and computer==2 or user=='gun' and computer==3:
        print("Tie match")
        print(f"Computer choose:{computer_choice}")
    elif user=='snake'and computer==2:
       print("YOU WIN !!!")
       print(f"Computer choose:{computer_choice}")
    elif user=='water'and computer==3:
       print("YOU WIN !!!")
       print(f"Computer choose:{computer_choice}")
    elif user=='gun'and computer==1:
       print("YOU WIN !!!")
       print(f"Computer choose:{computer_choice}")
    else:
       print('''YOU loose
             Try again
             good luck''')
       print(f"Computer choose:{computer_choice}")
       


