def counter(string, letter):
    count = 0
    for i in string:
        if letter == i:
            count += 1
    return count


string = input("Enter a string: ")
checkString = string.lower()
letter = input("Enter a letter to count: ")
checkLetter = letter.lower()
print("The number of times '{}' appeared in '{}' is {}".format(letter, string, counter(checkString, checkLetter)))
