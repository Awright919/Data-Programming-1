def computePay():
    if hours > 40:
        overtime = hours - 40
        nonOvertime = hours - overtime
        pay = (rate * nonOvertime) + (overtime * (rate * 1.5))
        return pay

    else:
        pay = hours * rate
        return pay


hours, rate = [float(x) for x in input().split()]
print(computePay())
