try:

    def calculate_average(grade, counter):
        total = 0
        for x in range(0, len(grade)):
            total = total + grade[x]
        calc_average = (total / counter) - 1
        return calc_average


    def get_letter(averages):
        if averages >= 90:
            letter = "A"
        elif 90 > averages >= 80:
            letter = "B"
        elif 80 > averages >= 70:
            letter = "C"
        elif 70 > averages >= 60:
            letter = "D"
        else:
            letter = "F"
        return letter


    def print_results(pnt_average, letter):
        print("Average: {}".format(pnt_average))
        print("Letter Grade: {}".format(letter))


    count = int(input("How many grades are you inputting?"))
    grades = [count]
    for i in range(0, count):
        grades.append(float(input("Enter grade {} :".format(i + 1))))
    average = calculate_average(grades, count)
    letters = get_letter(average)
    print_results(average, letters)

except ValueError:
    print("Error. Grade must be numeric.")
