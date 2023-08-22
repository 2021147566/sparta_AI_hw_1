import random


def main():
    """rock, paper, scissors game
    """

    while True:

        # win, tie, lose times
        wtl = [0, 0, 0]

        # player and computer choice
        player = input("Please choose rock, paper or scissors: ")
        comp = random.choice(['rock', 'paper', 'scissors'])

        # game rule
        try:
            if player.lower() == comp:
                print("Computer chose", comp)
                print("Tie!")
                wtl[1] += 1

            elif (player == 'scissors' and comp == 'paper') or\
                (player == 'rock' and comp == 'scissors') or\
                    (player == 'paper' and comp == 'rock'):
                print("Computer chose", comp)
                print("You win!")
                wtl[0] += 1

            elif (player == 'scissors' and comp == 'rock') or\
                (player == 'rock' and comp == 'paper') or\
                    (player == 'paper' and comp == 'scissors'):
                print("Computer chose", comp)
                print("You lose!")
                wtl[2] += 1

            # wrong input
            else:
                print("Error! Please input rock, paper or scissors!")

        # value error
        except ValueError:
            print("Error! Please input rock, paper or scissors!")

        # replay
        res = input("Do you want to play again? (y/n) ")
        # finish the game
        if res.lower() == 'n':
            False
            print("You have won", wtl[0], "times,", "tied",
                  wtl[1], "times,", "and lost", wtl[2], "times!")
            break


main()
