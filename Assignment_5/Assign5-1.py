import random
array = []
input = int(input("Enter number of elements:"))
for i in range(input):
    array.append(random.randint(1,100))

maxNum = max(array)
print('Max is  ', maxNum)
count = 0
for i in range(0, len(array),1):
    if array[i] == maxNum:
        count += 1
    if (i + 1) % 10 == 0:
        print(array[i])
    else:
        print(array[i], end=" ")

print("\nOccurrence of {} is {}".format(maxNum, count))

