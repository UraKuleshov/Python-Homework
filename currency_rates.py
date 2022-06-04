import requests
import json


# task 3
def currency_rates(currency):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    result = json.loads(response.text)
    registr = currency.isupper()
    currency_1 = 0
    if registr == False:
        currency_1 = currency.upper()
    else:
        currency_1 = currency
    try:
        res = f"Курс {currency_1} на {result['Date'][0:10]} по отношению к рублю " \
              f"составляет {result['Valute'][currency_1]['Value']}"
        print(res)
    except KeyError:
        print("None")
