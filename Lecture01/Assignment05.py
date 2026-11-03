talents = int(input("Enter number of talents: "))
pounds = int(input("Enter number of pounds: "))
lots = float(input("Enter number of lots: "))

total_grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("The weight in modern units")
print(kilograms, "kilograms and", round(grams, 2), "grams")