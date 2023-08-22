import random


def main():
    """guessing random number between 1 and 100 with up and down hints
    """

    # game: max attempts value
    game = 0
    while True:
        ans = random.randint(1, 100)
        count = 0

        while True:
            try:
                
                # new random number
                num = int(input("Please input a number between 1 and 100: "))
                
                # game rule
                if 1 <= num <= 100:
                    count += 1
                    if num > ans:
                        print("Down")
                    elif num < ans:
                        print("Up")
                    else:
                        print("Correct!")
                        print("You have tried", count, "times in total!")
                        game = max(game, count)
                        False
                        break
                    
                # out of range
                else:
                    print("Please input a number between 1 and 100")
                    
            # wrong input
            except ValueError:
                print("Please input a number between 1 and 100")

        # replay
        res = input("Do you want to play again? (y/n) ")

        # finish the game
        if res.lower() == 'n':
            print("You have tried", game, "times the most!")
            break


main()
