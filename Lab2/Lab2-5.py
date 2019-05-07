print("To convert from fahrenheit to celsius. Enter: 1")
print("To convert from celsius to fahrenheit. Enter: 2")
print("To convert from fahrenheit to kelvin. Enter: 3")
print("To convert from celsius to kelvin. Enter: 4")
userInput = int(input("Enter your decision: "))

if userInput == 1:
    temp = float(input("What is the temperature? "))
    celsius = (temp - 32) * (5 / 9)
    print("The temperature {} in celsius is {} degrees".format(temp, round(celsius, 3)))
    input()

if userInput == 2:
    temp = float(input("What is the temperature? "))
    fahrenheit = (temp * (9 / 5)) + 32
    print("The temperature {} in fahrenheit is {} degrees".format(temp, round(fahrenheit, 3)))
    input()

if userInput == 3:
    temp = float(input("What is the temperature? "))
    celsius = (temp - 32) * (5 / 9)
    kelvin = celsius + 273.15
    print("The temperature {} in kelvin is {} degrees".format(temp, round(kelvin, 3)))

if userInput == 4:
    temp = float(input("What is the temperature? "))
    kelvin = temp + 273.15
    print("The temperature {} in kelvin is {} degrees".format(temp, round(kelvin, 3)))
