import sqlite3
from typing import List


def execute_query(query_sql: str, db_path: str) -> List:
    '''
    Function to execute query the database in sqlite
    :param query_sql: query
    :param db_path: path to file.db
    :return: result of executed query
    '''
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: List) -> None:
    for record in records:
        print(*record)
