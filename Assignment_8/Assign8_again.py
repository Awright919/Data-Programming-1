

def load_data(input):
    count = 0
    with open(input, "r") as txt:
        with open("output.txt", "a") as file:
            for lines in txt:
                count += 1
                if lines.startswith("1"):
                    section_number = lines.split(",")[0]
                    prof_id = lines.split(",")[1]
                    student_id = lines.split(",")[2]
                    course_grade = lines.split(",")[3]
                    student_name = lines.split(",")[4]
                    course_id = lines.split(",")[5]
                    s_course_id = course_id.strip()
                    student_grade = find_number_grade(course_grade)
                    if course_grade == "W":
                        with open("Error.txt", "a") as error:
                            error.write(
                                "{}:  {}  {}  {} \n".format(section_number, prof_id, course_grade,
                                                            student_name, s_course_id))
                    else:
                        file.write(
                            "{}:  {}  {}  {}  {}  {}\n".format(student_name, s_course_id, section_number, prof_id,
                                                               course_grade, student_grade))
    return count


def get_prof_avg():
    with open("studentdata.csv", "r") as file:
        with open("Average.txt", "a") as average:
            average.write("Professor Average:\n")
            unique_list = []
            for line in file:
                professor = line.split(",")[1]
                if professor not in unique_list:
                    unique_list.append(professor)

        with open("Average.txt", "a") as average:
            number_grades = []
            for profs in unique_list:
                with open("studentdata.csv", "r") as new_file:
                    for new_line in new_file:
                        if new_line.split(",")[3] == "W":
                            continue
                        elif profs == new_line.split(",")[1]:
                            course_grade = new_line.split(",")[3]
                            temp = find_number_grade(course_grade)
                            number_grades.append(temp)
                    if len(number_grades) != 0:
                        professor_avg = sum(number_grades) / len(number_grades)
                        average.write("Professor {}: {}\n".format(profs, professor_avg))
                    number_grades.clear()


def get_student_avg():
    with open("studentdata.csv", "r") as file:
        with open("Average.txt", "a") as average2:
            average2.write("\nStudent Average:\n")
            unique_list = []
            for line in file:
                student = line.split(",")[4]
                if student not in unique_list:
                    unique_list.append(student)

        with open("Average.txt", "a") as average2:
            number_grades = []
            for student in unique_list:
                with open("studentdata.csv", "r") as new_file:
                    for new_line in new_file:
                        if new_line.split(",")[3] == "W":
                            continue
                        elif student == new_line.split(",")[4]:
                            course_grade = new_line.split(",")[3]
                            temp = find_number_grade(course_grade)
                            number_grades.append(temp)
                    if len(number_grades) != 0:
                        student_avg = sum(number_grades) / len(number_grades)
                        average2.write("Student {}: {}\n".format(student, student_avg))
                    number_grades.clear()


def get_section_avg():
    with open("studentdata.csv", "r") as file:
        with open("Average.txt", "a") as average3:
            average3.write("\nSection Average:\n")
            unique_list = []
            for line in file:
                section = line.split(",")[0]
                if section not in unique_list:
                    unique_list.append(section)

        with open("Average.txt", "a") as average3:
            number_grades = []
            for section in unique_list:
                with open("studentdata.csv", "r") as new_file:
                    for new_line in new_file:
                        if new_line.split(",")[3] == "W":
                            continue
                        elif section == new_line.split(",")[0]:
                            course_grade = new_line.split(",")[3]
                            temp = find_number_grade(course_grade)
                            number_grades.append(temp)
                    if len(number_grades) != 0:
                        student_avg = sum(number_grades) / len(number_grades)
                        average3.write("Section {}: {}\n".format(section, student_avg))
                    number_grades.clear()


def get_course_avg():
    with open("studentdata.csv", "r") as file:
        with open("Average.txt", "a") as average4:
            average4.write("\nCourse Average:\n")
            unique_list = []
            for line in file:
                course = line.split(",")[5].strip()

                if course not in unique_list:
                    unique_list.append(course)

        with open("Average.txt", "a") as average4:
            number_grades = []
            for course in unique_list:
                with open("studentdata.csv", "r") as new_file:
                    for new_line in new_file:
                        if new_line.split(",")[3] == "W":
                            continue
                        elif course == new_line.split(",")[5].strip():
                            course_grade = new_line.split(",")[3]
                            temp = find_number_grade(course_grade)
                            number_grades.append(temp)
                    if len(number_grades) != 0:
                        student_avg = sum(number_grades) / len(number_grades)
                        average4.write("Course {}: {}\n".format(course, student_avg))
                    number_grades.clear()


def find_number_grade(letter_grade):
    if letter_grade == "C":
        return 2.0
    elif letter_grade == "B":
        return 3.0
    elif letter_grade == "A":
        return 4.0
    else:
        return 1.0


open("output.txt", "w").close()
open("Average.txt", "w").close()
open("Error.txt", "w").close()
count = load_data("studentdata.csv")
get_prof_avg()
get_student_avg()
get_section_avg()
get_course_avg()
print("The number of lines scanned is {}.".format(count))
