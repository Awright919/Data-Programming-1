doc = input("Enter a file to scan : ")
keyword = "X-DSPAM-Confidence: "

with open(doc, "r") as file:
    count = 1
    total = 0
    float_num = 0
    for line in file:
        count += 1
        if line.startswith(keyword):
            total += 1
            con_pos = line.find(":")
            num = line[con_pos + 1:].strip()
            float_num += float(num)
print("The Average Spam Confidence is {}".format(float_num / total))