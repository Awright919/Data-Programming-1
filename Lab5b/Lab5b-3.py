num = int(input())
for i in range(1, num + 1, 1):
    print()
    for j in range(1, i, 1):
        print(" ", end= " ")
    for k in range(1, num + 1, 1):
        print(k, end=" ")
    for l in range(num - 1, 0, -1):
        print(l, end=" ")
    num -= 1
