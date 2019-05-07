from statistics import mean


def load_data(input):
    count = 0
    professors = set()
    students = set()
    courses = set()
    sections = set()
    prof_array = []
    list_professors = []
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
                    # writing to the output file
                    if course_grade == "W":
                        with open("Error.txt", "a") as error:
                            error.write(
                                "{}:  {}  {}  {} \n".format(section_number, prof_id, course_grade,
                                                            student_name, s_course_id))
                    else:
                        file.write(
                            "{}:  {}  {}  {}  {}  {}\n".format(student_name, s_course_id, section_number, prof_id,
                                                               course_grade, student_grade))
                    # adding to set to rid repeats
                    professors.add(str(prof_id))
                    students.add(student_name)
                    courses.add(s_course_id)
                    sections.add(section_number)

    list_professors = professors
    with open(input, "r") as read_file:
        with open("Averages.txt", "a") as average:
            average.write("Professor Average: \n")
            for prof in professors:
                for lines in read_file:
                    if lines.split(",")[3] == "W":
                        continue
                    elif prof in lines:
                        course_grade = lines.split(",")[3]
                        student_grade = find_number_grade(course_grade)
                        prof_array.append(student_grade)

                average.write("Professor {}: {} \n".format(prof, prof_array))

    return count


def find_number_grade(letter_grade):
    if letter_grade == "C":
        return 2.0
    elif letter_grade == "B":
        return 3.0
    elif letter_grade == "A":
        return 4.0
    else:
        return 1.0


count = load_data("studentdata.csv")
print("The number of lines scanned is {}.".format(count))
