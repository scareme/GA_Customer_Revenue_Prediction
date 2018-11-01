import json
from zipfile import ZipFile
import pandas as pd
from pandas.io.json import json_normalize


def df_json_convert(data, columns):
    for col in columns:
        df = json_normalize(data[col].apply(json.loads))
        df.columns = [f"{col}.{subcolumn}" for subcolumn in df.columns]
        data = data.drop(col, axis=1).merge(df, right_index=True,
                                            left_index=True)
    return data


def read_zip(zipfile, file, **kwards):
    with ZipFile(zipfile) as zip_file:
        with zip_file.open(file) as myfile:
            data = pd.read_csv(myfile, **kwards)
    return data
