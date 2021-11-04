# print("Hello world")
# print('Hello world')
# print('Let"s schedule a meeting')
# print("Hello\nWorld")
# print("""This is sentence 1.
# And this is a new paragraph.
# #######dshfsjdhfjshf
# And yet new line
# """)
# my_var = 5  # this is my var

# print("aaa", my_var, "bbb")

# "aaa"
# print(7*8-9)
# print("7*8-9=", 7*8-9)

# my_var = 5
# # print(f"7*8-9={7*8-9}")
# print(my_var)
# print("my_var")
# print(f"The value of my_var is: {my_var}")

# find max
# n1 = int(input())
# n2 = int(input())
#
# if n1 >= n2:
#     print(n1)
# else:
#     print(n2)
#
# print(max(n1, n2))

'''
Get string and print it in a beautiful way.
For example, get the string "world" and print
**********
* World! *
**********
'''
# word = input()
# print('*'*(len(word)+4))
# print('*', word, '*')
# print('*'*(len(word)+4))

# word = input()
# print(f"{'*'*(len(word)+4)}\n* {word} *\n{'*'*(len(word)+4)}")

# i1 = int(input())
# i2 = int(input())
# print(i1+i2)

# i = input()
# i = int(i)
# print(i)


# sum = 0
# n = int(input())
# sum = sum + n
# n = int(input())
# sum = sum + n
# n = int(input())
# sum = sum + n

# print(int(input()) + int(input()) + int(input()))


# val = input()
# # formatted = val.replace("T", "U")
# # formatted = formatted.replace("t", "u")
# formatted = val.replace("T", "U").replace("t", "u")
# print(formatted)


# val = input()
# val = val.upper()
# print(val[:3])
# print(val[3:6])
# print(val[6:9])

# COLLECTIONS - LISTS
# l = [92, 70, 57, 87, 100, 99, 85, 34, 65, 88]
# print(l)
# print(len(l))
# print("l[5:6] - ", l[5:6])
# print("l[5] - ", l[5])

# grades_list = []
# for i in range(5):
#     grade = input("Enter grade: ")
#     grades_list.append(grade)
#
# idx = int(input("Enter index: "))
# print(grades_list[idx-1])

grades_list = []
for i in range(5):
    grade = input("Enter grade: ")
    grades_list.append(grade)

for i in range(4, -1, -1):
    print(grades_list[i])

