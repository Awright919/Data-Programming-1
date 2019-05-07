integer = int(input("Enter an integer: "))
total = 0
while integer > 0:
    remainder = integer % 10
    total += remainder
    integer = integer // 10
print(total)

