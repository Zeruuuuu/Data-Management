import pandas as pd
import sys
import requests


def Get_Data(Low, High):   # Get data from firebase with requests
    Low_float = float(Low)
    High_float = float(High)
    url = 'https://dsci551-hw1-55f5f-default-rtdb.firebaseio.com/Cars.json?orderBy="price"&startAt=' + str(Low_float) + "&endAt=" + str(High_float)
    r = requests.get(url)
    return r.json()


def read_json(file):   # convert a json file to dataframe
    df = pd.DataFrame(data=file)
    return df.T


def Get_ID(df):    # return a list containing car_ID value after filtering
    if len(df) > 0:
        List = df['car_ID'].to_list()
        List.sort()
        return List
    else:
        return []


if __name__ == "__main__":     # Call all the functions above
    Low, High = sys.argv[1], sys.argv[2]
    json_file = Get_Data(Low, High)
    DataFrame = read_json(json_file)
    List = Get_ID(DataFrame)
    if len(List) > 0:
        print(f'IDs for the car price range are: {List}')
    else:
        print('No cars found with the given range')





