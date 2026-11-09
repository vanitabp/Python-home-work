numbers = []

while True:
    num = input("Enter a number(press enter to stop): ")

    if num == "":
        break
    numbers.append(float(num))
numbers.sort(reverse=True)

print("Five greatest numbers are: ")
for num in numbers[:5]:
    print(num)