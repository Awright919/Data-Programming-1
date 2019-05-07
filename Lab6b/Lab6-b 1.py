def reverse1(string):
    return string[::-1]


def reverse2(string):
    i = len(string)
    reverseName = ""
    while i > 0:
        reverseName += string[i - 1]
        i -= 1
    return reverseName


def isPalindrome1(string):
    rev = reverse1(string)
    if rev == string:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")


def isPalindrome2(string):
    rev = reverse2(string)
    if rev == string:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")


userInput = input("Enter something nice: ")
newInput = userInput.lower()
isPalindrome1(newInput)
isPalindrome2(newInput)
