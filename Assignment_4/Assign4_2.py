try:

    def calc_bmi(height, weight):
        bmi = (weight / height ** 2) * 703
        return bmi


    def getCategory(bmi):

        if bmi >= 30:
            print("obese")

        elif 25 <= bmi < 30:
            print("overweight")

        elif 18.5 <= bmi < 25:
            print("normal")

        else:
            print("underweight")

    def main():
        height, weight = [float(x) for x in input("Enter your height and weight? ").split()]
        bmi = calc_bmi(height, weight)
        print("BMI: {}".format(bmi))
        getCategory(bmi)

    if __name__ == "__main__":
        main()

except ValueError:
    print("This program only takes numeric input. Program terminated")
