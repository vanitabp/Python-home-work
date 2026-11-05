cabin = input("Enter cabin class (LUX, A, B, C): ")

if cabin == "LUX":
    print("Upper-desk cabin with a balcony. ")
elif cabin == "A":
    print("Cabin above the car desk with window. ")
elif cabin == "B":
    print("Windowless cabin above the car deck. ")
elif cabin == "C":
    print("Windowless cabin below the car desk. ")
else:
    print("Invalid cabin class. ")
