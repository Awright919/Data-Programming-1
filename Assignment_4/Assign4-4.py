from statistics import mean

try:
    def calcStats(array):
        minimum = min(array)
        maximum = max(array)
        range = maximum - minimum
        average = mean(array)

        return minimum, maximum, range, average
    count = int(input("How many numbers are you entering? "))
    array = []
    for i in range(0, count):
        array.append(float(input("Enter number {}: ".format(i + 1))))
    minimum, maximum, range, average = calcStats(array)
    print("Minimum: ${:,.2f}".format(minimum))
    print("Maximum: ${:,.2f}".format(maximum))
    print("Range: ${:,.2f}".format(range))
    print("Average: ${:,.2f}".format(average))
except ValueError:
    print("All inputs should be numeric")
