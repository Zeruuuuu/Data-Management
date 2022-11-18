import pandas as pd
import sys
import requests


def read_csv(file):    # read csv files
    csv_file = pd.read_csv(file)
    return csv_file


def To_json(csv_file):   # make dataframe json
    df = pd.DataFrame(csv_file)
    Json_file = df.to_json(orient='records')
    return Json_file


def To_firebase(Json_file):   # upload json file to firebase
    r = requests.put('https://dsci551-hw1-55f5f-default-rtdb.firebaseio.com/Cars.json', data = Json_file)


if __name__ == "__main__":   # Call functions above
    File_name = sys.argv[1]
    csv_file = read_csv(File_name)
    Json_file = To_json(csv_file)
    To_firebase(Json_file)



