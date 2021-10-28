# exersice 10 from hw

# num = int(float(input()))
# print(((num//2) + 1) * 2)



# conditions
# num = int(input("Enter number: "))
# if num != 0:
#     print("Not Zero")
# else:
#     print("zero")


# page 17 exercise 4
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 % num2 == 0:
#     print("num1 can bve divided by num2")
# if num2 % num1 == 0:
#     print("num2 can bve divided by num1")

# page 17 exercise 5
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 < num2:
#     print(num1, num2)
# else:
#     print(num2, num1)

# page 17 exercise 6
# option 1
# name = input("Enter name: ")
# salary = int(input("Enter salary: "))
# new_salary = salary * 1.1
# if new_salary > 6000:
#     new_salary = salary * 1.05
# print(new_salary)

#option 2
# name = input("Enter name: ")
# salary = int(input("Enter salary: "))
# new_salary = salary * 1.1
# if new_salary > 6000:
#     new_salary = salary * 1.05
#     print(new_salary)
# else:
#     print(new_salary)


# num = int(input("Enter number: "))
# if num >= 0:
#     if num == 0:
#         print("zero")
#     else:
#         if num > 100:
#             print("> 100")
#         else:
#             print("<= 100")
#         print("positive")
# else:
#     if num <= -100:
#         print("negative less than -100")
#     else:
#         print("negative more than -100")

# page 18 ex 4
# num = int(input("Enter number between 1 - 9999: "))
# if num < 10:
#     print("1 digit")
# else:
#     if num < 100:
#         print("2 digits")
#     else:
#         if num < 1000:
#             print("3 digits")
#         else:
#             print("4 digits")


# age = int(input("age: "))
# height = int(input("height: "))
# if (age >= 18 and height > 100) or (8 <= age < 18 and height > 115):
#     print("ok")
# else:
#     print("no")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if num1 <= num2 and num1 <=num3:
#     # num1 is the minimum
#     print(num1)
#     if num3 <= num2:
#         print(num3, num2)
#     else:
#         print(num2, num3)
# else:
#     # eiter num2 or num3 is minimum
#     if num2 <= num1 and num2 <= num3:
#         # num2 is the minimum
#         print(num2)
#         if num3 <= num1:
#             print(num3, num1)
#         else:
#             print(num1, num3)
#     else:
#         # num3 is the minimum
#         print(num3)
#         if num1 <= num2:
#             print(num1, num2)
#         else:
#             print(num2, num1)

# page 20 ex 4
# year = int(input("Enter a year: "))
# if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
#     print('not leap')
# else:
#     print('leap')


# page 20 ex 5
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# if month != 2:
#     if (month <= 7 and month % 2 == 1) or (month > 7 and month % 2 == 0):
#         print("31 days")
#     else:
#         print("30 days")
# else:
#     if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
#         print("28 days")
#     else:
#         print("29 days")

# while
# num = int(input("Enter number"))
# while num > 0:
#     print(num)
#     num = num - 1

# num = int(input("Enter number: "))
# while num % 10 != 0:
#     num = int(input("Re-enter number: "))
# print("You're good")

# password = input("Enter password: ")
# count = 1
# while password != "python" and count < 3:
#     count = count + 1
#     password = input("Re-enter password: ")
#
# if password == "python":
#     print("Logged in")
# else:
#     print("Try again later")

# page 25 ex 2
# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))
# if num1 <= num2:
#     minimum = num1
#     maximum = num2
# else:
#     maximum = num1
#     minimum = num2
#
# while minimum <= maximum:
#     print(minimum)
#     minimum += 1

# page 25 ex 3
# n = int(input("Enter a number: "))
# current = 0
# while current <= n:
#     print(current)
#     current = current + 2

# page 25 ex 4
# max = int(input("Enter max: "))
# den = int(input("Enter den: "))
# current = 1
# while current <= max:
#     if (current % den) == 0:
#         print(current)
#     current = current + 1

# page 26 ex. 9
n = int(input())
max = n
idx = 1
max_idx = 1

while idx < 3:
    idx += 1
    n = int(input())
    if n > max:
        max_idx = idx
        max = n
print(max_idx)