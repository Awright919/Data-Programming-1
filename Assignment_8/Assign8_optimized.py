def load_data(input):
    count = 0
    list_prof, list_student, list_section, list_course, document = ([] for i in range(5))
    with open(input, "r") as doc:
        for lines in doc:
            document.append(lines)

    for line in document:
        count += 1
        if line.split(",")[0] not in list_section:
            list_section.append(line.split(",")[0])
        if line.split(",")[1] not in list_prof:
            list_prof.append(line.split(",")[1])
        if line.split(",")[4] not in list_student:
            list_student.append(line.split(",")[4])
        if line.split(",")[5].strip() not in list_course:
            list_course.append(line.split(",")[5].strip())

    return count, list_prof, list_student, list_section, list_course, document


def print_avg(professors, students, sections, courses, document):
    average = []
    with open("Average.txt", "a") as file:
        # Professors
        file.write("Professor Average: \n")
        for profs in professors:
            for line in document:
                if line.split(",")[3] == "W":
                    continue
                elif profs == line.split(",")[1]:
                    average.append(find_number_grade(line.split(",")[3]))
            file.write("Professor {} : {}\n".format(profs, (sum(average) / len(average))))
            average.clear()
            # Students
        file.write("\n Student Average:\n")
        for stu in students:
            for line in document:
                if line.split(",")[3] == "W":
                    continue
                elif stu == line.split(",")[4]:
                    average.append(find_number_grade(line.split(",")[3]))
            if len(average) != 0:
                file.write("Student {} : {}\n".format(stu, (sum(average) / len(average))))
            average.clear()
            # Course
        file.write("\n Course Average:\n")
        for cour in courses:
            for line in document:
                if line.split(",")[3] == "W":
                    continue
                elif cour == line.split(",")[5].strip():
                    average.append(find_number_grade(line.split(",")[3]))
            file.write("Courses {} : {}\n".format(cour, (sum(average) / len(average))))
            average.clear()
            # Section
        file.write("\n Section Average:\n")
        for sect in sections:
            for line in document:
                if line.split(",")[3] == "W":
                    continue
                elif sect == line.split(",")[0]:
                    average.append(find_number_grade(line.split(",")[3]))
            file.write("Section {} : {}\n".format(sect, (sum(average) / len(average))))
            average.clear()


def find_number_grade(letter_grade):
    if letter_grade == "C":
        return 2.0
    elif letter_grade == "B":
        return 3.0
    elif letter_grade == "A":
        return 4.0
    else:
        return 1.0


open("Average.txt", "w").close()
count, professors, students, sections, courses, document = load_data("studentdata.csv")
print_avg(professors, students, sections, courses, document)
print("The number of lines scanned is {}".format(count))
