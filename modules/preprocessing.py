import json
from zipfile import ZipFile
from datetime import datetime

import pandas as pd
from pandas.io.json import json_normalize


def df_json_convert(data, columns):
    for col in columns:
        df = json_normalize(data[col].apply(json.loads))
        df.columns = [f"{col}.{subcolumn}" for subcolumn in df.columns]
        data = data.drop(col, axis=1).merge(df, right_index=True,
                                            left_index=True)
    return data


def show_json_example(example, stopword=None):
    for key, value in json.loads(example).items():
        if stopword:
            if stopword != value:
                print(f'{key}: {value}')
        else:
            print(f'{key}: {value}')


def read_zip(zipfile, file, **kwards):
    with ZipFile(zipfile) as zip_file:
        with zip_file.open(file) as myfile:
            data = pd.read_csv(myfile, **kwards)
    return data


def timestamp_to_str(df_column):
    convert_dict = {
        el: datetime.utcfromtimestamp(int(el))
        for el in df_column.unique()
    }
    return df_column.map(convert_dict)


def return_year(df_column):
    convert_dict = {
        el: datetime.utcfromtimestamp(int(el)).year
        for el in df_column.unique()
    }
    return df_column.map(convert_dict)


def return_month(df_column):
    convert_dict = {
        el: datetime.utcfromtimestamp(int(el)).month
        for el in df_column.unique()
    }
    return df_column.map(convert_dict)


def return_day(df_column):
    convert_dict = {
        el: datetime.utcfromtimestamp(int(el)).day
        for el in df_column.unique()
    }
    return df_column.map(convert_dict)


def return_hour(df_column):
    convert_dict = {
        el: datetime.utcfromtimestamp(int(el)).hour
        for el in df_column.unique()
    }
    return df_column.map(convert_dict)


def return_date(df_column):
    convert_dict = {}
    for key in df_column.unique():
        year = str(datetime.utcfromtimestamp(int(key)).year)
        month = datetime.utcfromtimestamp(int(key)).month
        month = str(month) if month > 9 else '0' + str(month)
        day = datetime.utcfromtimestamp(int(key)).day
        day = str(day) if day > 9 else '0' + str(day)
        convert_dict[key] = int(year + month + day)
    return df_column.map(convert_dict)
