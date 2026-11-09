inches = float(input("Enter inches : "))

while inches >= 0:
    cm = inches * 2.54
    print(f"{cm:.2f}, cm")
    inches = float(input("Enter inches (negative number to stop): "))


print("Program stopped.")

