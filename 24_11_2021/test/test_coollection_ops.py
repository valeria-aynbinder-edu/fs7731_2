from utils.collection_ops import convert_dict_to_list

grades = {
    'Valeria': {
        'math': [90, 100, 95],
        'english': [87, 90]
    },
    'Ravit': {
        'sport': [90, 97],
        'biology': [100]
    }
}

def test_len():
    new_list = convert_dict_to_list(grades)
    assert(len(grades) == len(new_list))
    # if (len(grades) != len(new_list)):
    #     print("test_len failed")
    # else:
    #     print("test_len passed")

def test_elems_type():
    new_list = convert_dict_to_list(grades)
    for elem in new_list:
        if type(elem) is not dict:
            print("test_elems_type failed")
            return
    print("test_elems_type passed")

if __name__ == '__main__':
    test_len()
    test_elems_type()