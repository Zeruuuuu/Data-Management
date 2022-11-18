import sys
import json


def format_float(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num


def extract_str_int(n):
    value = list(n.values())[0]
    if [j for j in n][0] == 'S':
        return value
    elif [j for j in n][0] == 'N':
        return format_float(float(value))


def extract_list(l):
    my_list = []
    for ele in list(l.values())[0]:
        my_list.append(extract_str_int(ele))
    return my_list


def extract_map(m):
    my_map = {}
    values = list(m.values())[0]
    keys = [j for j in values]
    for j in keys:
        my_map[j] = extract_str_int(values[j])
    return my_map


def extract_num_set(n):
    l = list(n.values())[0]
    return [format_float(float(j)) for j in l]


def extract_str_set(s):
    l = list(s.values())[0]
    return [j for j in l]


def get_pruned(key, value):
    pruned_values = []
    for i in value:
        if [j for j in i][0] in ['S', 'N']:
            pruned_values.append(extract_str_int(i))
        elif [j for j in i][0] == 'L':
            pruned_values.append(extract_list(i))
        elif [j for j in i][0] == 'M':
            pruned_values.append(extract_map(i))
        elif [j for j in i][0] == 'NS':
            pruned_values.append(extract_num_set(i))
        else:
            pruned_values.append(extract_str_set(i))
    my_dict = {}
    for i in key:
        for j in pruned_values:
            my_dict[i] = j
            pruned_values.remove(j)
            break
    return my_dict


if __name__ == '__main__':
    v1 = sys.argv[1]
    v2 = sys.argv[2]
    f = open(v1)
    data = json.load(f)
    key_list = []
    for i in data:
        key_list.append(i)
    value_list = []
    for key in key_list:
        value_list.append(data[key])
    my_dict = get_pruned(key_list, value_list)
    with open(v2, 'w') as outfile:
        json.dump(my_dict, outfile)



