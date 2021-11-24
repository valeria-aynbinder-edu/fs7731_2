# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from utils.math_ops import get_divisors
# from utils.validators import is_number
from utils.validators import is_number


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    get_divisors(5)
    is_number("5")
    from utils import imported_modules
    # print(imported_modules)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
