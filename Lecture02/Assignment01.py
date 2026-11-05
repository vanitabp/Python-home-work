length = float(input("Enter the length of the zander in cm: "))
limit = 42
if length < 42:
    short = 42 - length
    print("Release the fish back into the lake.")
    print(f"The fish is {short} cm short of the legal limit. ")
else:
    print("You can keep the fish. ")
