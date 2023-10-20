from utils.sqlite_tools.conversions.csv2sqlite import *
import pytest

params_test_sql_create_table_statement_from_header = [
    ("test1", ["col1", "col2", "col3"], "CREATE TABLE test1(col1, col2, col3)")
]

@pytest.mark.parametrize('name,header,expected', params_test_sql_create_table_statement_from_header)
def test_sql_create_table_statement_from_header(name, header, expected):
    actual = sql_create_table_statement_from_header(name, header)
    
    assert actual == expected
