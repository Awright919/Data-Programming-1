userInput = input("Enter a string: ")
end = userInput.find(":")
number = float(userInput[end + 1:])
print(userInput)
print(number, type(number))

