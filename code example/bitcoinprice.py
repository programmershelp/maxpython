import requests # http://docs.python-requests.org/en/master/

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

data = response.json()
#print(data)
print("1 Bitcoin is worth")
print(data["bpi"]["USD"]["rate"] + " Dollars")
print(data["bpi"]["EUR"]["rate"] + " Euros")
print(data["bpi"]["GBP"]["rate"] + " Pounds")