import requests
import json
import csv

key = 'D57064T4IGI17THK'
ticker = 'FB'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}&datatype=csv'.format(ticker, key)
response = requests.get(url)
data = response.text
#print(response.json())

#with open('jsonDump.json', 'w') as jsonFile:
#    json.dump(jsonData, jsonFile)

#csvData = jsonData['Time Series (Daily)']
with open('fb_daily.csv','w') as csvfile:
    csvfile.write(data)

#print(str(csvData))
