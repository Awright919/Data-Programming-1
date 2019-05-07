userInput = int(input("Enter an integer: "))
total = 1

for i in range(1, userInput + 1):
    total = i + 1 / total
print(total)
