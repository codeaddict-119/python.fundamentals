import random

def get_user_choice():
    print("Choose one:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        return "Rock"
    elif choice == "2":
        return "Paper"
    elif choice == "3":
        return "Scissors"
    else:
        return None

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    
    if user_choice is None:
        print("Invalid choice. Please run the game again.")
        return
    
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

play_game()