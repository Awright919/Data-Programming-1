from Assignment_4 import Assign4_2


class person:
    def __init__(self, name="Jim", age="20", cholesterol="low", height="60", weight="150"):
        self.name = name
        self.age = age
        self.cholesterol = cholesterol
        self.height = height
        self.weight = weight

    def whatName(self):
        return self.name

    def whatAge(self):
        return self.age

    def whatCholesterol(self):
        return self.cholesterol

    def whatHeight(self):
        return self.height

    def whatWeight(self):
        return self.weight


def main(string):
    count = (string.count(" ") + 1)
    persons = [count]
    personal_record = [count]
    for i in count:
        persons[i] = string.split(" ")
    for j in count:
        name, age, cholesterol, height, weight = persons[j].split(",")
        personal_record[j] = person(name, age, cholesterol, height, weight)
    for k in count:
        print("{}: {}".format(personal_record[k].whatName(),
                              Assign4_2.calc_bmi(personal_record[k].whatHeight(), personal_record[k].whatWeight())))


main(input("Enter a string: "))

