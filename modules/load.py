from zipfile import ZipFile
import pandas as pd


def read_zip(zipfile, file, **kwards):
    zip_file = ZipFile(zipfile)
    return pd.read_csv(zip_file.open(file), **kwards)
