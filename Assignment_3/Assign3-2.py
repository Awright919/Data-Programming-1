day1, day2, day3, day4, day5, age = [float(x) for x in input().split()]
if age >= 18:
    total = day1 + day2 + day3 + day4 + day5
    average = total / 5
    if 18 <= age <= 65:
        if average < 7:
            print("Average: {}".format(average))
            print("Sleep: too little")
        elif average > 9:
            print("Average: {}".format(average))
            print("Sleep: too much")
        else:
            print("Average: {}".format(average))
            print("Sleep: normal")

    elif age >= 65:
        if average < 7:
            print("Average: {}".format(average))
            print("Sleep: too little")
        elif average > 8:
            print("Average: {}".format(average))
            print("Sleep: too much")
        else:
            print("Average: {}".format(average))
            print("Sleep: normal")
else:
    print("You must be an adult to participate")
