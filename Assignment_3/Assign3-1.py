bloodPressure, cholesterol = [float(x) for x in input().split()]
if bloodPressure >= 140:
    print("Systolic Blood Pressure: {}, Stage 2 Hypertension".format(bloodPressure))

elif 130 <= bloodPressure < 140:
    print("Systolic Blood Pressure: {}, Stage 1 Hypertension".format(bloodPressure))

elif 120 <= bloodPressure < 130:
    print("Systolic Blood Pressure: {}, Elevated".format(bloodPressure))

else:
    print("Systolic Blood Pressure: {}, Normal".format(bloodPressure))

if cholesterol >= 240:
    print("Total Cholesterol: {}, High".format(cholesterol))

elif 200 <= cholesterol < 240:
    print("Total Cholesterol: {}, Borderline High".format(cholesterol))

else:
    print("Total Cholesterol: {}, Desirable".format(cholesterol))

