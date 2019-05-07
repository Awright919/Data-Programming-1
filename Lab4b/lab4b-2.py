def computeGrade(userInput):
    if userInput < 0.0 or userInput > 1.0:
        print("Bad Score")

    elif userInput >= 0.9:
        print("A")

    elif 0.9 > userInput >= 0.8:
        print("B")

    elif 0.8 > userInput >= 0.7:
        print("C")

    elif 0.7 > userInput >= 0.6:
        print("D")

    elif userInput < 0.6:
        print("F")

    else:
        print("Bad Score.")


try:
    userInput = float(input("Enter a number between 0.0 and 1.0 (inclusive): "))
    computeGrade(userInput)


except ValueError:
    print("Bad Score. Restart the program.")
