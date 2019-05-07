height, weight = [float(x) for x in input().split()]
bmi = (weight / (height**2)) * 703
print(bmi)
