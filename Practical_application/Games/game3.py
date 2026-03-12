import random

def display_menu():
    print("\n===== ROCK PAPER SCISSORS =====")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Exit")

def get_user_choice():
    while True:
        display_menu()
        choice = input("Enter your choice (0/1/2/3): ")

        if choice == "1":
            return "Rock"
        elif choice == "2":
            return "Paper"
        elif choice == "3":
            return "Scissors"
        elif choice == "0":
            return None
        else:
            print("Invalid input! Please try again.")

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "User"
    else:
        return "Computer"

def print_round_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if winner == "Tie":
        print("It's a tie!")
    elif winner == "User":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()

        if user_choice is None:
            print("\nThanks for playing!")
            break

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        print_round_result(user_choice, computer_choice, winner)

        if winner == "User":
            user_score += 1
        elif winner == "Computer":
            computer_score += 1

        print("\nCurrent Score:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")

def main():
    print("Welcome to Rock Paper Scissors Game!")
    play_game()

if __name__ == "__main__":
    main()