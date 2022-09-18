from flask import Flask, request

from utils import get_currency_exchange_rate

app = Flask(__name__)


@app.route('/exchange_rates', methods=['GET'])
def get_rate():
    date = request.args.get('date', default='01.09.2022')
    currency_base = request.args.get('currency_base', default='UAH')
    currency_exchange = request.args.get('currency_exchange', default='USD')
    bank = request.args.get('bank', default='NB')
    result = get_currency_exchange_rate(date, currency_base, currency_exchange, bank)
    return result
