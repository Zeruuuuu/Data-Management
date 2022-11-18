import sys
import requests
import re


def get_data():  # get data from firebase
    r = requests.get('https://dsci551-hw1-55f5f-default-rtdb.firebaseio.com/Index.json')
    my_dict = r.json()
    return my_dict


def convert_to_list(key):       # Convert the input keywords into a list
    my_list = re.split('[!"#$%&()*+, -./:;<=>?@[\]^_`{|}~]', key)
    for i in range(len(my_list)):
        my_list[i] = my_list[i].lower()
    my_list = list(filter(None, my_list))
    return my_list


def judge(my_list, my_dict):   # test how many keywords that a car_name has
    is_in = False
    value_list = []
    contained_element = []
    for i in my_list:
        if i in my_dict.keys():
            is_in = True          # if any keys detected, then there is cars found.
            contained_element.append(i)
    if not is_in:
        return 'No cars found'
    else:
        for j in contained_element:
            value_list.extend(my_dict[j])
        value_list = sorted(value_list, key=value_list.count, reverse=True)   # sort base on number of occurrence
        value_list = list(dict.fromkeys(value_list))     # remove duplicated but remain sequence
        return f'IDs of the car are: {value_list}'


if __name__ == "__main__":
    Key = sys.argv[1]
    my_dict = get_data()
    my_list = convert_to_list(Key)
    returned = judge(my_list, my_dict)
    print(returned)



