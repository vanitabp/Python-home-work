
numbers = []

while True:
    value = input("Enter a number: ")

    if value == "":
        break

    numbers.append(float(value))

    if len(numbers) > 0:
        print(f"smallest number is : {min(numbers)} ")
        print(f"largest number is : {max(numbers)} ")
    else :
        print("No numbers entered")