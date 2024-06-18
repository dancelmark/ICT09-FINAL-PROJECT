import random


def rock_paper_scissors():
    moves = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while player_score < 2 and computer_score < 2:
        player_move = input("Enter rock, paper, or scissors: ").lower()
        computer_move = random.choice(moves)

        print(f"Computer chose {computer_move}")

        if player_move == computer_move:
            print("It's a tie!")
        elif (player_move == "rock" and computer_move == "scissors") or \
                (player_move == "paper" and computer_move == "rock") or \
                (player_move == "scissors" and computer_move == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    if player_score == 2:
        print("You win the game!")
    else:
        print("Computer wins the game!")


rock_paper_scissors()
