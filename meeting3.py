# print("Solution to p. 26, ex. 22")
#
# value = int(input("Enter a number: "))
#
# prev_element = 1
# current_element = 1
#
# # print two first (default) elements
# print(prev_element)
# print(current_element)
#
# sum = prev_element + current_element
#
# while sum <= value:
#     print(sum)
#     prev_element = current_element
#     current_element = sum
#     sum = prev_element + current_element
#
# # need to add this in order to print the last element larger than value
# print(sum)

#######################################################
####################### p. 27, ex. 28 #################
#######################################################

# print("Solution to p. 27, ex. 28")
#
# sum_2000 = 0
# count = 0
#
# while count < 5:
#     count = count + 1
#     # count += 1
#     temp = int(input("Enter temperature for July 2000: "))
#     sum_2000 = sum_2000 + temp
#     # sum_2000 += temp
#
#
# # we received all the temperatures of July 2020, now we can calculate avg
# avg_2000 = sum_2000 / count
# print("Average temp in July 2020: ", avg_2000)
#
# # set count to 0 again to start receiving temperatures for July 2021
# count = 0
#
# # start getting temperatures for July 2001
# while count < 5:
#     count = count + 1
#     temp = int(input("Enter temperature for July 2001: "))
#     if temp > avg_2000:
#         print("The temperature in July, ", count, " was higher than average of July 2000")

# sum = 0
# for i in range(10):
#     n = int(input())
#     sum = sum + n
# print(sum/i)

# sum = 0
# count = 0
# while count < 10:
#     n = int(input())
#     sum = sum + n
#     count = count + 1
# print(sum/count)

# value of STOP is 30 (by default adds 1, starts from 0)
# for i in range(30):
#     print(i)
#
# # value of START is 3, STOP is 30 (by default adds 1)
# for i in range(3, 30):
#     print(i)
#
# # value of START is 3, STOP is 30, STEP is 4
# for i in range(3, 30, 4):
#     print(i)

# decreasing
# for i in range(30, 3, -4):
#     print(i)

# b = 32
# c = -b
# for a in range(b, 0, c):
#     print("c:", c)
#     c = int(c/2)
#     b = b-8
#
# print(b)

# p 31 ex 3
# n = int(input())
#
# factorial = 1
#
# #will enter into the loop as long as i < n+1 => i<=n
# for i in range(1, n+1, 1):
#     factorial = factorial * i
# print(factorial)


# p32 ex 11
# n1 = int(input())
# n2 = int(input())
#
# if n1 <= n2:
#     min = n1
#     max = n2
# else:
#     max = n1
#     min = n2
#
# for i in range(min, max):
#     print(i)
# for i in range(max, min-1, -1):
#     print(i)
#
# #p 33 ex 15
# sum = 0
# count = 0
# for i in range(100):
#     name = input('Name: ')
#     grade = int(input('Grade: '))
#     if grade > 70:
#         print(name)
#         sum = sum + grade
#         count = count + 1
# if count == 0:
#     print("Avg: ", 0)
# else:
#     print("Avg: ", sum/count)

# p 33 ex 18
# review later
# max_num = 0
# second_max_num = 0
# max_index = 0
# second_max_index = 0
#
# amount = int(input())
#
# if amount == 1:
#     print("Error")
#     exit(1)
#
# for i in range(1, amount+1):
#     n = int(input())
#
#     if i == 1:
#         max_num = n
#         max_index = i
#     elif i == 2:
#         if n >= max_num:
#             second_max_num = max_num
#             second_max_index = max_index
#             max_num = n
#             max_index = i
#     else:
#         if second_max_num <= n < max_num:
#             second_max_num = n
#             second_max_index = i
#         else:
#             if n > max_num:
#                 second_max_num = max_num
#                 second_max_index = max_index
#                 max_num = n
#                 max_index = i
#
# print("Second largest: ", second_max_num)
# print("Index: ", second_max_index)


# sum = 0
#
# n = int(input())
#
# for i in range(n):
#     sum = i + sum
#     if sum >= n:
#         break
#
# print("the sum is ", sum)

# while True:
#     num = int(input())
#     if num == 0:
#         break

# sum = 0
# for i in range(5):
#     n = int(input())
#     if i % 3 != 0:
#         continue
#     sum = sum + n

# page 35, ex 4
# total_for = 0
# total_against = 0
# total_absteined = 0
# for i in range(170):
#     vote = int(input())
#     if vote == 1:
#         total_for += 1
#     elif vote == 2:
#         total_against +=1
#     elif vote == 3:
#         total_absteined += 1
#     else:
#         print("Vetto from ", i)
#         exit()
# print("Total for: ", total_for, " Total against: ", total_against, " Total absteined: ", total_absteined)


# nested loops
# inner_loop_count = 0
# for i in range(5):
#     n = int(input("Enter number: "))
#
#     while n >= 10:
#         n = n // 10
#         inner_loop_count += 1
#     print("Most significant digit: ", n)
# print("Inner loop ran ", inner_loop_count)

# for i in range(10):
#     for j in range (10):
#         print(i, " ",j)

# page 29 ex 3
# num = int(input("Enter num: "))
# while num >= 0:
#     digits_sum = 0
#     temp = num
#     while temp > 0:
#         rightmost_digit = temp % 10
#         temp = temp // 10
#         digits_sum = digits_sum + rightmost_digit
#     print("Digits sum of : ", num, " is: ", digits_sum)
#     num = int(input("Enter num: "))

# page 38 ex. 8
# rows = int(input("Enter rows: "))
# cols = int(input("Enter columns: "))
# for i in range(rows):
#     for j in range(cols):
#         print("*", end=" ")
#     print()

# page 38 ex. 15
start_year = 1991
end_year = 1993
months_per_year = 3

max_annual_rainfall = 0
max_monthly_rainfall = 0

max_annual_rainfall_year = 1991
max_monthly_rainfall_month = 1
max_monthly_rainfall_year = 1991

for year in range(start_year, end_year+1):

    total_rainfall_per_year = 0

    for month in range(1, months_per_year+1):
        rainfall = int(input(f"Enter rainfall for month {month} year {year}: "))
        if rainfall >= max_monthly_rainfall:
            max_monthly_rainfall = rainfall
            max_monthly_rainfall_month = month
            max_monthly_rainfall_year = year
        total_rainfall_per_year += rainfall

    if max_annual_rainfall <= total_rainfall_per_year:
        max_annual_rainfall = total_rainfall_per_year
        max_annual_rainfall_year = year

print("Rainiest year was ", max_annual_rainfall_year)
print("Rainiest month was ", max_monthly_rainfall_month, " of ", max_monthly_rainfall_year)
