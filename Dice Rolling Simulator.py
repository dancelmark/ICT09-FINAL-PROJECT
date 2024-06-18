import random


def roll_dice(player):
    input(f"{player}, press Enter to roll the dice...")
    roll = random.randint(1, 6)
    print(f"{player} rolled a {roll}")
    return roll


def play_round(player1, player2):
    print(f"\nRound starts now!")

    player1_roll = roll_dice(player1)
    player2_roll = roll_dice(player2)

    if player1_roll > player2_roll:
        print(f"{player1} wins this round!")
        return player1
    elif player2_roll > player1_roll:
        print(f"{player2} wins this round!")
        return player2
    else:
        print("It's a tie!")
        return None


def main():
    player1 = "Player 1"
    player2 = "Player 2"

    player1_wins = 0
    player2_wins = 0
    rounds = 3

    for i in range(1, rounds + 1):
        print(f"\n--- Round {i} ---")
        winner = play_round(player1, player2)

        if winner == player1:
            player1_wins += 1
        elif winner == player2:
            player2_wins += 1

        if player1_wins == 2 or player2_wins == 2:
            break

    print("\nGame Over")
    if player1_wins > player2_wins:
        print(f"{player1} wins the game!")
    else:
        print(f"{player2} wins the game!")


if __name__ == "__main__":
    main()

