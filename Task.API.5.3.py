import requests
currencies = requests.get('https://api.coinbase.com/v2/currencies')
e_rates = requests.get('https://api.coinbase.com/v2/exchange-rates')

currencies_format = currencies.json()
currencies_data = currencies_format['data']

x = input("Enter the currency name : ")


def search(x, currencies_data):
    return [element for element in currencies_data if element['name'] == x]

lam = search(x,currencies_data)
print(lam)

interchange = lam[0]
print(interchange)

print("NOTE: All exchange rates are with respect to USD")

access = interchange['id']
print('id = ' + access)

print('Currency = ' +x)

e_rates_format = e_rates.json()
e_rates_data = e_rates_format['data']['rates'][access]
print('Exchange rate = ' + e_rates_data)

dash = '-'
OHLC = access + dash + x
print(OHLC)
