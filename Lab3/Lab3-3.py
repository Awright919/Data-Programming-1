try:
    userInput = float(input("Enter a number between 0.0 and 1.0 (inclusive): "))

    if userInput < 0.0 or userInput > 1.0:
        print("Bad Score")
        userInput = float(input("Try again: "))

    if userInput >= 0.9:
        print("A")

    if 0.9 > userInput >= 0.8:
        print("B")

    if 0.8 > userInput >= 0.7:
        print("C")

    if 0.7 > userInput >= 0.6:
        print("D")

    if userInput < 0.6:
        print("F")

    else:
        print("Bad Score.")

except ValueError:

    print("Bad Score. Restart the program.")

