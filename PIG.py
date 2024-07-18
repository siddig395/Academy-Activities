import random 

def roll():
    min_value = 1
    max_value = 18
    roll = random.randint(min_value, max_value)

    return roll 
while True:
    players = input("Enter the number of players (2-8): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 8:
            break
        else:
             print("Must be between 2 - 8 players.")
    else:
            print("invalid, try again again")

max_score = 100
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0 

        while True:
            should_roll = input("Would you like to roll (y/n)? ")
            if should_roll.lower() != "y":
                break
    
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_score.index(max_score)
print("player number", winning_idx + 1, "is the winner with a score of:", max_score)
