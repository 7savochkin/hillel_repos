from datetime import datetime

import requests


def get_currency_iso_code(currency: str) -> int:
    currency_dict = {
        'UAH': 980,
        'USD': 840,
        'EUR': 978,
        'GBP': 826,
        'JPY': 392,
        'CHF': 756,
        'CNY': 156,
        'PLN': 985
    }
    try:
        return currency_dict[currency]
    except:
        raise KeyError('Currency not found! Update currency information.')


def get_currency_exchange_rate(currency_a: str,
                               currency_b: str):
    currency_code_a = get_currency_iso_code(currency_a)
    currency_code_b = get_currency_iso_code(currency_b)

    responce = requests.get('https://api.monobank.ua/bank/currency')
    json_currency = responce.json()

    if responce.status_code == 200:
        for i in range(len(json_currency)):
            if json_currency[i].get('currencyCodeA') == currency_code_a and json_currency[i].get(
                    'currencyCodeB') == currency_code_b:
                date = datetime.fromtimestamp(
                    int(json_currency[i].get('date'))
                ).strftime('%Y-%M-%D %h:%m:%s')
                rate_sell = json_currency[i].get('rateSell')
                rate_buy = json_currency[i].get('rateBuy')
                return f'Exchange rate {currency_a} to {currency_b} for {date}: \n rate sell - {rate_sell}' \
                       f' \n rate buy - {rate_buy}'
        return f'Not found: {currency_a} to {currency_b}'
    else:
        return f'ApiError {responce.status_code}: {json_currency.get("errorDescription")}'