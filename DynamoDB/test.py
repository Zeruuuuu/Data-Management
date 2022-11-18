import json


f = open('input.json')
data = json.load(f)
key_list = []
for i in data:
    key_list.append(i)
value_list = []
for key in key_list:
    value_list.append(data[key])


def extract_str_int(n):
    value = list(n.values())[0]
    if [j for j in n][0] == 'S':
        return value
    elif [j for j in n][0] == 'N':
        return float(value)


def extract_list(l):
    my_list = []
    for ele in l:
        my_list.append(extract_str_int(ele))


for i in list(value_list[4].values())[0]:
    print(i)

