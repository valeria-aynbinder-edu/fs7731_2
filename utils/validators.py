print("inside validators")

from utils import imported_modules

imported_modules.append(__name__)

def is_number(text):
    """
    This function receives a string and check whether it is a number
    :param text: string
    :return: True if number, False otherwise
    """
    return text.isdigit()


def is_in_range(range_start, range_end, num):
    return range_start <= num <= range_end


def remove_leading_dash(text):
    if text.startswith("-"):
        text = text[1:]
    return text


def is_decimal_number(text):
    # first of all, remove leading "-" if exists
    text = remove_leading_dash(text)

    # check whether this is a float
    if "." in text:
        dot_idx = text.index(".")
        # remove everything after dot
        int_part = text[:dot_idx]
        decimal_part = text[dot_idx+1:]
        return is_number(int_part) and is_number(decimal_part)
    else:
        return False

def is_negative_number(text):
    starts_with_neg = text.startswith("-")
    text = remove_leading_dash(text)
    return starts_with_neg and (is_number(text) or is_decimal_number(text))

