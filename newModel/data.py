import requests
import json

key = 'D57064T4IGI17THK'
ticker = 'FB'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
response = requests.get(url)
print(response.json())
