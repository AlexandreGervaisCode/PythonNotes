# I didn't follow BroCode's version

def rps():
    import random
    hasWon = False
    while not hasWon:
        options = ["rock","paper","scissors"]
        cpu = random.choice(options)
        player = None
        while player not in options:
            player = input("Choose Rock, Paper or Scissors ").lower()

        textWon = "You have chosen {} and the cpu chose {}, you win".format(player, cpu)
        textLose = "You have chosen {} and the cpu chose {}, you lose".format(player, cpu)

        if player == cpu:
            print("You both chose " + player)

        elif player == "rock":
            if cpu == "paper":
                print(textLose)

            elif cpu == "scissors":
                print(textWon)
                hasWon = True

            else:
                print("Rock ERROR")

        elif player == "paper":
            if cpu == "rock":
                print(textWon)
                hasWon = True

            elif cpu == "scissors":
                print(textLose)

            else:
                print("Paper ERROR")

        elif player == "scissors":
            if cpu == "paper":
                print(textWon)
                hasWon = True

            elif cpu == "rock":
                print(textLose)

            else:
                print("Scissors ERROR")

        else:
            print("Game ERROR")
