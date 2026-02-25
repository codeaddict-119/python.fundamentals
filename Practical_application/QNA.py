"""
Mini Linux Quiz
"""

<<<<<<< HEAD
elif ans.lower=="yes":
       import os 
       filepath="c:\Users\Admin\Documents\GitHub\python.fundamentals\QNA.py"# add you file path here 
       try:
              os.remove(filepath)
              print("The LINUX is a kernal not OS," \
              "wrong answer your file will be deleted now" \
              )
       except FileNotFoundError:
              print("File not found")
else:
<<<<<<< HEAD
       print("That wasnt a yes or no... even Bash would be confused.")
=======
       print("That wasn't a yes or no... even Bash would be confused.")
>>>>>>> 3081e107dd614d420553d7d1323aae80074abae7
=======
def ask_question():
    print("Answer the following question:")
    print("Is Linux a full operating system by itself? (yes/no)")
    
    ans = input("Your answer: ").strip().lower()

    if ans == "no":
        print("Correct.")
        print("Linux is a kernel. A complete operating system is typically built using the Linux kernel along with tools like GNU.")
    
    elif ans == "yes":
        print("Incorrect.")
        print("Linux by itself is only a kernel, not a complete operating system.")
    
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")

def bonus_question():
    print("\nBonus Question:")
    print("What does the kernel primarily manage?")
    print("1. Hardware resources")
    print("2. Web browsing")
    print("3. Text editing")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        print("Correct. The kernel manages hardware resources like CPU, memory, and devices.")
    elif choice in ["2", "3"]:
        print("Incorrect. The kernel is responsible for managing hardware resources.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    ask_question()
    bonus_question()
>>>>>>> 4d69bc6c44cef9cae05611611c3c671ff42bdd63
