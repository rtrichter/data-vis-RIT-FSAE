import sqlite3
import pandas as pd

def sql_create_table_statement_from_header(name: str, header: list[str]) -> str:
    columns = ", ".join(header)
    return f"CREATE TABLE {name}({columns})"

separators = {
    "csv": ',',
    "tsv": '\t',
    "psv": '|'
}
def csv2sqlite(csv_path: str, separator=None, db_path=None) -> None:
    no_extension = "".join(csv_path.split('.')[:-1])
    name = no_extension.split("/")[-1]
    if separator is None:
        extension = csv_path.split('.')[-1]
        separator = separators[extension]
    if db_path is None:
        # replace the file extension and save in the same place
        db_path = "".join(csv_path.split('.')[:-1]) + ".db"
    # load the csv
    df = pd.read_csv(csv_path, sep=separator)
    # make a connection
    db = sqlite3.connect(db_path)
    # make a cursor
    cur = db.cursor()
    # insert all of the data appropriately
    cur.execute(sql_create_table_statement_from_header(name, df.columns))
    # write the database
    statement = f"""INSERT INTO {name} VALUES({(("?, "*len(df.values[0]))[:-2])})"""
    # without using tolist we get byte objects instead of typed values
    cur.executemany(statement, df.values.tolist())

    db.commit()
    db.close()
    return db_path