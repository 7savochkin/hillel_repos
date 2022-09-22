from flask import Flask, request

from utils_db import get_filter_customers, count_firstname_customers_sql, count_firstname_customers_python, \
    get_total_amount_of_orders_sql, get_total_amount_of_orders_py

app = Flask(__name__)

@app.route('/customers', methods=['GET'])
@app.route('/filtered_customers', methods=['GET'])
def get_customers():
    state = request.args.get('state', default=None)
    city = request.args.get('city', default=None)
    result = get_filter_customers(state, city)
    return result


@app.route('/sql_count')
@app.route('/sql_count_firstname')
def get_count_first_name_sql():
    result = count_firstname_customers_sql()
    return result


@app.route('/py_count')
@app.route('/py_count_firstname')
def get_count_first_name_py():
    result = count_firstname_customers_python()
    return result


@app.route('/sql_orders')
@app.route('/sql_total_amount_orders')
def get_total_amount_sql():
    result = get_total_amount_of_orders_sql()
    return result


@app.route('/py_orders')
@app.route('/py_total_amount_orders')
def get_total_amount_py():
    result = get_total_amount_of_orders_py()
    return result
