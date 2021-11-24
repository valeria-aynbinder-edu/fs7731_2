from utils.math_ops import *
from utils.validators import *

if __name__ == '__main__':
    while True:

        user_input = input("Insert a number between 1 and 100: ")
        if not is_number(user_input):
            print("You did not insert a valid number, please try again")
            continue

        # if we got here, the inserted string is a number
        num = int(user_input)
        if not is_in_range(1, 100, num):
            print("Your number is out of the range of [1, 100], please try again")
            continue

        all_divisors = get_divisors(num)
        print(f"The number you entered {num} has the following divisors: {all_divisors}")
        print(f"Prime number: {is_prime(num)}")