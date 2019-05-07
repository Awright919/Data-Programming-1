num = int(input())
for i in range(num, 0, -1):
    print()
    for j in range(1, i):
        print(" ", end= " ")
    for k in range(1, num - i + 2 ):
        print(k, end=" ")
    for k in range(num - i, 0, -1):
        print(k, end=" ")

