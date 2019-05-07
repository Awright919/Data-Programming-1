file_name = input("Enter a filename: ")
keyword = "From"
count = 0
with open(file_name, "r") as file:
    with open("Output.txt", "a") as output:
        for lines in file:
            if lines.startswith(keyword):
                count += 1
                junk = lines.split()[0]
                output.write(lines.split()[1] + "\n")
print("{} emails were in the document. ".format(count))
with open("Output.txt", "r") as output:
    with open("Output_No_Dupes.txt", "a") as new_output:
        email_set = set(output.readlines())
        for x in email_set:
            new_output.write(x)
