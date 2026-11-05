gender = input("Enter your biological gender (M/F): ")
hemoglobin = float(input("Enter your hemoglobin level (g/L): "))

if gender == "F":
    if hemoglobin < 117:
        print("Hemoglobin is low.")
    elif hemoglobin > 155:
        print("Hemoglobin is high.")
    else:
        print("Hemoglobin is normal.")

elif gender == "M":
    if hemoglobin < 134:
       print("Hemoglobin is low.")
    elif hemoglobin > 167:
        print("Hemoglobin is high.")
    else:
        print("Hemoglobin is normal.")

else:
    print("Invalid gender.")