print("inside math_ops")
import math
from utils import imported_modules

imported_modules.append(__name__)

pi=3.14

def get_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def is_prime(num):
    divisors = get_divisors(num)
    return len(divisors) == 2


def get_sqrt(num):
    return math.sqrt(num) == int(math.sqrt(num)), math.sqrt(num)