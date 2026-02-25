import os

def ask_question():
    print("--- Mini Linux Quiz ---")
    print("Is Linux a full operating system by itself? (yes/no)")
    
    ans = input("Your answer: ").strip().lower()

    if ans == "no":
        print("\nCorrect!")
        print("Linux is technically a kernel. A complete OS (like Ubuntu or Fedora) "
              "is built by combining the kernel with GNU tools and other software.")
    
    elif ans == "yes":
        print("\nIncorrect.")
        # Logic for the 'file deletion' joke/warning
        filepath = r"c:\Users\Admin\Documents\GitHub\python.fundamentals\QNA.py" 
        
        print("The Linux core is a kernel, not a full OS.")
        
        # We wrap this in a try-except to handle cases where the file doesn't exist
        try:
            # os.remove(filepath) # Uncomment this ONLY if you actually want to delete the file!
            print(f"DEBUG: I would have deleted {filepath} now.")
        except FileNotFoundError:
            print("File not found, so nothing was deleted.")
    
    else:
        print("\nThat wasn't a yes or no... even Bash would be confused.")

def bonus_question():
    print("\nBonus Question:")
    print("What does the kernel primarily manage?")
    print("1. Hardware resources")
    print("2. Web browsing")
    print("3. Text editing")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        print("Correct! The kernel manages CPU, memory, and hardware devices.")
    elif choice in ["2", "3"]:
        print("Incorrect. Those are applications; the kernel manages the hardware underneath.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    ask_question()
    bonus_question()