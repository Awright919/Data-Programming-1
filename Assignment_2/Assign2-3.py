try:
    original, rate, numberOfYears, compoundsPerYear = [float(x) for x in input().split()]
    if 0 > rate or rate > 100:
        print("Not a valid rate. (Between 0 and 100 inclusive)")
        input()
        exit()
    if compoundsPerYear > 365:
        print("Not a valid number of payments. (Between 1 and 365 inclusive")
        input()
        exit()
    if 0 <= rate <= 100 and 1 <= compoundsPerYear <= 365:
        interest = (original * (1 + ((rate / 100) / compoundsPerYear)) ** (compoundsPerYear * numberOfYears)) - original
        print("Interest paid:", interest)

except ValueError:
    print("All inputs should be numeric")


