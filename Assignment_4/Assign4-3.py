try:

    def calcInterest(original, rate, compoundsPerYear, numberOfYears):
        interest = (original * (1 + ((rate / 100) / compoundsPerYear)) ** (compoundsPerYear * numberOfYears)) - original
        return interest

    original, rate, numberOfYears, compoundsPerYear = [float(x) for x in input().split()]
    if 0 <= rate <= 100 and 1 <= compoundsPerYear <= 365:
        interest = calcInterest(original, rate, numberOfYears, compoundsPerYear)
        print("Interest: ${:,.2f}".format(interest - original))
    else:
        print("Be sure your rate is between 0 and 100 and your compounds per year is between 1 and 365")
except ValueError:
    print("All inputs should be numeric")


