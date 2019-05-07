with open("romeo.txt", "r") as file:
    file_words = []
    new_list = []
    with open("Lab 8_Output.txt", "a") as output:
        for lines in file:
            for word in lines.split():
                if word in file_words:continue
                file_words.append(word)
        new_list = sorted(file_words)
        for lines in new_list:
            output.write(lines + "\n")
