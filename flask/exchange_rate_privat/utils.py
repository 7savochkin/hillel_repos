import requests

def get_currency_exchange_rate(date: str, currency_base: str,
                               currency_exchange: str, bank: str) -> str:
    api_privatbank = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    response = requests.get(api_privatbank)
    json_rate = response.json()
    if response.status_code == 200:
        exchange_rate = json_rate['exchangeRate']
        for index in range(len(exchange_rate)):
            if exchange_rate[index].get('baseCurrency') == currency_base and exchange_rate[index].get(
                    'currency') == currency_exchange:
                if bank == 'NB':
                    rate_sell = exchange_rate[index].get('saleRateNB')
                    rate_buy = exchange_rate[index].get('purchaseRateNB')
                    return f'NBU exchange rate for {date} when converting ' \
                           f'{currency_base} to {currency_exchange}: \n' \
                           f'rate sell - {rate_sell} \n' \
                           f'rate buy - {rate_buy}'
                elif bank == 'PB':
                    rate_sell = exchange_rate[index].get('saleRate')
                    rate_buy = exchange_rate[index].get('purchaseRate')
                    return f'PrivatBank exchange rate for {date} when converting ' \
                           f'{currency_base} to {currency_exchange}: \n' \
                           f'rate sell - {rate_sell} \n' \
                           f'rate buy - {rate_buy}'
                else:
                    return f'Not found: {bank}'
        return f'Not found: {currency_base} to {currency_exchange}'
    else:
        return f'ApiError {response.status_code}: {json_rate.get("errorDescription")}'
      
