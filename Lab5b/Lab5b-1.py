num = int(input())
for i in range(num, 0, -1):
    print()
    for j in range(1, i):
        print(" ", end= "")
    for k in range(0, num - i + 1 ):
        print("*", end="")

