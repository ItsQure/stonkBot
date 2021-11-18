import requests
import json
import csv

key = 'D57064T4IGI17THK'
ticker = 'FB'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
response = requests.get(url)
#print(response.json())
jsonData = response.json()
with open('jsonDump.json', 'w') as f:
    json.dump(jsonData,f)

csvData = jsonData['Time Series (Daily)']
csvFile = open('fb_daily.csv','w')
#print(str(csvData))
"""
count = 0
for item in csvData:
    if count == 0:
        headers = item.keys()
        csvFile.writerow(headers)
        count+=1
    csvFile.writerow(item.values())

csvFile.close()
"""
