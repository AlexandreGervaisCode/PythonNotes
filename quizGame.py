# Kinda just copies BroCode's code

def newGame():
    guesses = []
    correctAnswers = 0
    questionNum = 1

    for key in questions:
        print("---------------------------------------------------------------------------")
        print(key)
        for i in choiceOptions[questionNum-1]:
            print(" {:450}".format(i))
        guess = input("Enter either 'A', 'B', 'C' or 'D'").upper()
        guesses.append(guess)
        correctAnswers += chkAnswer(questions.get(key),guess)
        questionNum += 1

    scoreDisplay(correctAnswers, guesses)


def chkAnswer(ans, gss):
    if ans == gss:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

def scoreDisplay(correct, gss):
    print("---------------------------------------------------------------------------")
    print("{:^70}".format("RESULTS"))
    print("---------------------------------------------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in gss:
        print(i, end=" ")
    print()

    score = int((correct/len(questions)*100))
    print("Your score is {}% ! ".format(score))

def replay():
    response = input("Do you want to play again ? ").lower()
    if response == "yes":
        return True
    elif response == "no":
        return False

questions = {
    "What year was the most famous bite?: ": "D",
    "A famous artist from Germany ": "B",
    "Famous canadian Twitch streamer 'SmallAnt' changed his last name to what?: ": "C",
    "Complete this quote from famous Youtuber and Twitch streamer 'TommyInnit' with the missing last word: 'Just killed a woman, feeling '": "A"
}

choiceOptions = [["A. 1983", "B. 1991","C. 2005","D. 1987"],
                 ["A. DaVinci", "B. Adolf Hitler", "C. Van Goh", "D. Albert Einstein"],
                 ["A. Ant", "B. Wooper", "C. Minecraft", "D. Gamer"],
                 ["A. good", "B. bad", "C. satisfied", "D. epic"]]

newGame()

while replay():
    newGame()

print("Thank you for playing")
