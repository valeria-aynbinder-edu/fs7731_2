#######################################################
####################### p. 18, ex. 5 ##################
#######################################################

print("Solution to p. 18, ex. 5")

salary = int(input("Enter salary: "))

# stores the total amount of tax that should be payed
total_tax = 0

# Calculate tax for level 1
level1_amount = 23000
if salary < 23000:
    level1_amount = salary
total_tax = total_tax + level1_amount * 0.1

if salary > 23000:
    # Calculate tax for level 2
    level2_amount = 74000 - 23000
    if salary < 74000:
        level2_amount = salary - 23000
    total_tax = total_tax + level2_amount * 0.2

    if salary > 74000:
        # Calculate tax for level 3
        level3_amount = 100000 - 74000
        if salary < 100000:
            level3_amount = salary - 74000
        total_tax = total_tax + level3_amount * 0.3

        if salary > 100000:
            # Calculate tax for level 4
            level4_amount = 200000 - 100000
            if salary < 200000:
                level4_amount = salary - 100000
            total_tax = total_tax + level4_amount * 0.4

            if salary > 200000:
                # Calculate tax for level 5
                level5_amount = salary - 200000
                total_tax = total_tax + level5_amount * 0.5

print("Total tax to pay: ", total_tax)


#######################################################
####################### p. 20, ex. 2 ##################
#######################################################

print("Solution to p. 20, ex. 2")

grade = int(input("Enter a grade: "))

if grade < 55:
    print("Not enough")
else:
    if grade >= 55 and grade <= 64:
        print("Enough")
    else:
        if grade >= 65 and grade <= 74:
            print("Almost good")
        else:
            if grade >= 75 and grade <= 84:
                print("Good")
            else:
                if grade >= 85 and grade <= 94:
                    print("Very good")
                else:
                    print("Great")

#######################################################
####################### p. 25, ex. 6 ##################
#######################################################

print("Solution to p. 25, ex. 6")

sum = 0
count = 0

number = int(input("Enter a number: "))

while number != 0:
    # add to sum and to count
    sum = sum + number
    count = count + 1

    # get a new number from the user
    number = int(input("Enter a number: "))

# In case the first and only input was "0", need to check in order to prevent division by zero!
if count == 0:
    print("The average is 0")
else:
    print("The average is: ", sum/count)


#######################################################
####################### p. 26, ex. 19 #################
#######################################################

print("Solution to p. 26, ex. 19")

number = int(input("Enter a number: "))
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1

print("The factorial is ", factorial)



#######################################################
####################### p. 26, ex. 22 #################
#######################################################

print("Solution to p. 26, ex. 22")

value = int(input("Enter a number: "))

prev_element = 1
current_element = 1

# print two first (default) elements
print(prev_element)
print(current_element)

sum = prev_element + current_element

while sum < value:
    print(sum)
    prev_element = current_element
    current_element = sum
    sum = prev_element + current_element

# need to add this in order to print the last element larger than value
print(sum)


#######################################################
####################### p. 27, ex. 28 #################
#######################################################

print("Solution to p. 27, ex. 28")

sum_2000 = 0
count = 0

while count < 5:
    count = count + 1
    temp = int(input("Enter temperature for July 2000: "))
    sum_2000 = sum_2000 + temp


# we received all the temperatures of July 2020, now we can calculate avg
avg_2000 = sum_2000 / count
print("Average temp in July 2020: ", avg_2000)

# set count to 0 again to start receiving temperatures for July 2021
count = 0

# start getting temperatures for July 2001
while count < 5:
    count = count + 1
    temp = int(input("Enter temperature for July 2001: "))
    if temp > avg_2000:
        print("The temperature in July, ", count, " was higher than average of July 2000")
