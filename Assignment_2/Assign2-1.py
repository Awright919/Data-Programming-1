
try:
    grade1, grade2, grade3 = [float(x) for x in input().split()]
    average = ((grade1 * 0.15) + (grade2 * 0.20) + (grade3 * 0.65))

    if average >= 90:
        print("Average: {}".format(average))
        print("Letter Grade: A")
    if 90 > average >= 80:
        print("Average: {}".format(average))
        print("Letter Grade: B")
    if 80 > average >= 70:
        print("Average: {}".format(average))
        print("Letter Grade: C")
    if 70 > average >= 60:
        print("Average: {}".format(average))
        print("Letter Grade: D")
    if average < 60:
        print("Average: {}".format(average))
        print("Letter Grade: F")
except ValueError:
    print("Enter a correct input. Restart the program.")
