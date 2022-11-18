import sys
import pandas as pd
import requests
import re
import json


def to_dataframe(filename):
    df = pd.read_csv(filename)
    return df


def get_key(df):       # Get the list of car_IDs
    key_list = []
    for key in df['CarName']:
        List = re.split('[!"#$%&()*+, -./:;<=>?@[\]^_`{|}~]', key)
        for i in range(len(List)):
            List[i] = List[i].lower()
        key_list.extend(List)
    key_set = set(key_list)
    new_list = list(key_set)
    return new_list


def make_dict(key_list, df):        # Create dictionary that contains keyword and list of car_IDs
    my_dict = {}
    for k in key_list:
        my_dict[k] = []
    for i in key_list:
        for key in df['CarName']:
            List = re.split('[!"#$%&()*+, -./:;<=>?@[\]^_`{|}~]', key)
            for j in range(len(List)):
                List[j] = List[j].lower()
            if i in List:
                keys = df.loc[df['CarName'] == key, 'car_ID']
                my_dict[i].extend(keys)
    value_list = list(my_dict.values())    # Trying to remove duplicated values
    key_list = list(my_dict.keys())
    value_list1 = []
    for i in value_list:
        i_new = list(set(i))
        value_list1.append(i_new)
    my_dic = {}
    for key in key_list:                 # Create a new dictionary without duplicates
        for value in value_list1:
            my_dic[key] = value
            value_list1.remove(value)
            break
    return my_dic


def to_json(my_dict):         # convert the dictionary into json file
    file = json.dumps(my_dict)
    return file


def to_firebase(file):   # upload json file to firebase
    r = requests.put('https://dsci551-hw1-55f5f-default-rtdb.firebaseio.com/Index.json', data=file)
    return r


if __name__ == "__main__":    # call functions above
    filename = sys.argv[1]
    df = to_dataframe(filename)
    key_list = get_key(df)
    my_dict = make_dict(key_list, df)
    del my_dict['']
    file = to_json(my_dict)
    r = to_firebase(file)





