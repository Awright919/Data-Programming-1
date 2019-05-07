doc = input("Enter a document to open in the directory: ")
with open(doc, "r") as file:
    for line in file:
        print(line.capitalize(), end=" ")
