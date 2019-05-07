vowels = ["a", "e", "i", "o", "u"]
cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
userInput = str(input("Enter Something Nice: "))
newInput = userInput.lower()
vowelCount = 0
conCount = 0
otherCount = 0
for i in newInput:
    if i in vowels:
        vowelCount += 1
    elif i in cons:
        conCount += 1
    else:
        otherCount += 1
print("There are {} vowels, {} consonants, and {} other types of characters (including spaces) in '{}'".format(vowelCount, conCount, otherCount, userInput))