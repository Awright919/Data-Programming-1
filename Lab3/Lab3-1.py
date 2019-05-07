try:
    hours, rate = [float(x) for x in input().split()]

    if hours > 40:
        overtime = hours - 40
        nonOvertime = hours - overtime
        pay = (rate * nonOvertime) + (overtime * (rate * 1.5))
        print(pay)

    else:
        pay = hours * rate
        print(pay)

except ValueError:
    print("Wrong numbers")
