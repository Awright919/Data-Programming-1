import sys


def calc_bmi(height, weight):
    bmi = (weight / height ** 2) * 703
    return bmi


def getCategory(bmi):
    if bmi >= 30:
        return"obese"

    elif 25 <= bmi < 30:
        return"overweight"

    elif 18.5 <= bmi < 25:
        return"normal"

    else:
        return"underweight"


for i in range(1, len(sys.argv)):
    name = sys.argv[i].split(",")[0]
    capName = name.capitalize()
    height = int(sys.argv[i].split(",")[3])
    weight = int(sys.argv[i].split(",")[4])
    bmi = calc_bmi(height, weight)
    category = getCategory(bmi)
    print("{}: {:.2f} , {}".format(capName, bmi, category))
