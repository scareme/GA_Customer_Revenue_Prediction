from datetime import datetime


class DateInfo:

    def __init__(self, df_column):
        self.convert_dict = {
            el: datetime.utcfromtimestamp(int(el))
            for el in df_column.unique()
        }
