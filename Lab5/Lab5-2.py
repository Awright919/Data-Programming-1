
array = []
while True:
    try:
        userInput = input("Enter a number: ")
        if userInput == "done":
            break
        array.append(float(userInput))

    except ValueError:
        print("Invalid Input")
        continue

print(sum(array))
print(max(array))
print(min(array))
print(len(array))
