original, rate, numberOfYears, compoundsPerYear = [float(x) for x in input().split()]

A = (original * (1 + ((rate / 100) / compoundsPerYear))**(compoundsPerYear * numberOfYears)) - original
print("Interest Paid: ", A)
