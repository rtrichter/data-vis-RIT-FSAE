import pandas as pd
from globals import SEPARATORS

def csv(csv_path: str, separator=None) -> pd:
    if separator is None:
        extension = csv_path.split('.')[-1]
        separator = SEPARATORS[extension]
    if db_path is None:
        # replace the file extension and save in the same place
        db_path = "".join(csv_path.split('.')[:-1]) + ".db"
    # load the csv
    df = pd.read_csv(csv_path, sep=separator)
    return df