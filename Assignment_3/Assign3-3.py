try:
    q1, q2, q3, q4 = [float(x) for x in input().split()]
    total = q1 + q2 + q3 + q4
    print("${:,.2f}, ${:,.2f}, ${:,.2f}, ${:,.2f}".format(q1, q2, q3, q4))
    print("Total Sales: ${:,.2f}".format(total))
    if total >= 150000:
        print("Sales: High")
    elif 50000 <= total < 150000:
        print("Sales: med")
    elif 20000 <= total < 50000:
        print("Sales: low")
    elif total < 20000:
        print("Sales: low")
        print("Warning: Need to improve sales.")

except ValueError:
    print("All sales should be numeric")
