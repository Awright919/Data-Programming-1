import random

luckyNumber = random.randint(10, 99)
d1LuckyNumber = luckyNumber // 10
d2LuckyNumber = luckyNumber % 10
print(luckyNumber)
guessedNumber = int(input("Enter a two digit number: "))
d1GuessedNumber = guessedNumber // 10
d2GuessedNumber = guessedNumber % 10

oneMatched = False
twoMatched = False
exactMatch = False

if (d1LuckyNumber == d1GuessedNumber) and (d2LuckyNumber == d2GuessedNumber):
    exactMatch = True

elif (d1LuckyNumber == d2GuessedNumber) and (d2LuckyNumber == d1GuessedNumber):
    twoMatched = True

elif (d1LuckyNumber == d1GuessedNumber or d1LuckyNumber == d2GuessedNumber) or \
        (d2LuckyNumber == d1GuessedNumber or d2LuckyNumber == d2GuessedNumber):
    oneMatched = True

if exactMatch:
    print("Your award is $10,000")
elif twoMatched:
    print("Your award is $3,000")
elif oneMatched:
    print("Your award is $1,000")
else:
    print("No award")



