# Get a number from the user
# cake = int(input("Cake"))
# kids = int(input("Kids"))
# each = int(cake/kids)
# left = cake % kids
# print(f"Each: {each}, left: {left}")


# Tutorial 2
# width = int(input("Enter width: "))
# length = int(input("Enter length: "))
# perimiter = 2 * (width + length)
# area = width * length
# print("Area: ", area, "Perimiter: ", perimiter)


# Tutorial 4
# total_minutes = int(input("Enter minutes: "))
# hours = int(total_minutes / 60)
# minutes = total_minutes % 60
# print(hours, "h", minutes, "min")


# Tutorial 6
num = int(input("Enter number (at least 4 digits): "))
# calculate "tens" number
temp = num % 100
# operator // returns result of division without decimal point
result = temp // 10
print("The second digit from right is: ", result)