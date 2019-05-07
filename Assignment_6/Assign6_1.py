def main(string):
    desirableCount = string.count("Desirable") + string.count("desirable")
    borderlineCount = string.count("Borderline") + string.count("borderline")
    highCount = string.count("High") + string.count("high")

    print("Desirable Count: {}".format(desirableCount))
    print("Borderline Count: {}".format(borderlineCount))
    print("High Count: {}".format(highCount))


main(input("Enter a string: "))
