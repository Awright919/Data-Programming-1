try:
    list = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "done"or user_input == "Done" or user_input == "DONE":
            print("Maximum: {}".format(max(list)))
            print("Minimum: {}".format(min(list)))
            break
        else:
            number = int(user_input)
            list.append(number)
            continue
except ValueError:
    print("Only enter a number or the word 'done'")
    print("Program Exiting")
