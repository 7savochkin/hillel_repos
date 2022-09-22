import os
from typing import List

from utils import execute_query


def get_filter_customers(state: str, city: str) -> List:
    '''
    Returns customers filtered by city and state
    :param state: state
    :param city: city
    :return: client's list
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    query_sql = '''
        SELECT *
            FROM customers
    '''
    if state and city:
        query_sql += f"WHERE State = '{state}' AND City = '{city}'"
    elif state:
        query_sql += f"WHERE State = '{state}'"
    elif city:
        query_sql += f"WHERE City = '{city}'"
    return execute_query(query_sql, db_path)


def count_firstname_customers_sql() -> List:
    '''
    Returns first name and ones count repeating. Using SQL
    :return: first name and count repeating
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    query_sql = '''
        SELECT FirstName, COUNT(FirstName) 
            FROM customers
        GROUP BY FirstName;
    '''
    return execute_query(query_sql, db_path)


def count_firstname_customers_python() -> List:
    '''
    Returns first name and one's count repeating. Using Python
    :return: first name and count repeating
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    query_sql = '''
          SELECT FirstName
              FROM customers;
      '''
    list_names = [elem[0] for elem in execute_query(query_sql, db_path)]
    list_names.sort()
    result = [(name, list_names.count(name)) for name in list_names]
    return result


def get_total_amount_of_orders_sql() -> List:
    '''
    Returns total amount orders. Using SQL
    :return: total amount of orders
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    query_sql = '''
        SELECT SUM(UnitPrice*Quantity) 
	        FROM invoice_items
    '''
    return execute_query(query_sql, db_path)


def get_total_amount_of_orders_py() -> List:
    '''
    Returns total amount orders. Using Python
    :return: total amount orders
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    query_sql = '''
        SELECT UnitPrice, Quantity
            FROM invoice_items
    '''
    total_amount = [elem[0]*elem[1] for elem in execute_query(query_sql, db_path)]
    result = [(sum(total_amount),)]
    return result