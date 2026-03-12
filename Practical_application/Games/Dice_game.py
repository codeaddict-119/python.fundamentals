import random

def rool():
       min_value=1
       max_value=6
       rool=random.randint(min_value,max_value)
       
       return rool

while True:
       players=input("Enter the number of players (1-4):")
       if players .isdigit():
              players=int(players)
              if 1<= players <=4:
                     break
              else:
                     print("NUmber must be between 1 and 4")
       else:  
              print("Invalid Input")       


max_score=50
player_scores=[0 for _ in range(len(players))]

while max(player_scores)<max_score:
       for player_idx in range(players):
              print("\nPlayer number",player_idx +1,"turn has started!\n")
              current_score=0

              while True:
                     should_rool=input("Would you like to rool (y)?")
                     if should_rool.lower() !="y":
                            break

                     value=rool()
                     if value==1:
                            print("You rolled a 1! Turn over")
                            current_score=0
                            break
                     else:
                            current_score+=value
                            print("You rolled a :",value)
                     
                     print("Your score is:",current_score)
              
              player_scores[player_idx] += current_score
              print("Your total score is :",player_scores[player_idx])

max_score=max(player_scores)
win_idx=player_scores.index(max_score)
print("Player number",win_idx +1,
      "is the winner with a score of :",max_score)