try:
    bmi = float(input())
    if bmi < 18.5:
        print("BMI category is underweight")
    if 18.5 <= bmi < 25:
        print("BMI category is normal")
    if 25 <= bmi < 30:
        print("BMI category is overweight")
    if bmi >= 30:
        print("BMI category is obese")
except ValueError:
    print("This program only takes numeric input. Program terminated.")
