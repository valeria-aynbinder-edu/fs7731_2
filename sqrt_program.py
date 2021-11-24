from utils.math_ops import *
from utils.validators import *


def print_sqrt_msg(num):
    is_int_sqrt, sqrt = get_sqrt(num)
    if is_int_sqrt:
        print(f"The number {num} has integer sqrt: {sqrt}")
    else:
        print(f"The number {num} does not have integer sqrt")


# print(f"The value of attribute __name__ is {__name__}")


if __name__ == '__main__':
    while True:
        user_input = input("Enter a number: ")

        if is_negative_number(user_input):
            print(f"No sqrt for negative number {user_input}. Try again.")
            continue

        if is_decimal_number(user_input):
            num = float(user_input)
            print_sqrt_msg(num)
            continue

        if is_number(user_input):
            num = int(user_input)
            print_sqrt_msg(num)
            continue

        print("Invalid input. Try again")