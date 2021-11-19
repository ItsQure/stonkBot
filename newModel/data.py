import requests
import json
import csv
from pandas_datareader import data
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt

#Alphavantage API usages
key = 'D57064T4IGI17THK'
ticker = 'FB'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=full&apikey={}&datatype=csv'.format(ticker, key)
response = requests.get(url)

#convert to Response object to text for file writing.
data = response.text
#Write csv data locally -- read write permissions (old files will be overwritten with the w+ permission paramater)
csvfile = open('fb_daily.csv', 'w+')
formattedCSV = open('fb_formatted.csv','w+')
csvfile.write(data)
#df = pd.DataFrame(columns=['Date','Low','High','Close','Open'])

csvRead = csv.reader(csvfile)
tempCsv = csv.writer(formattedCSV)
for row in csvRead:
    if any(row):
        tempCsv.writerow(row)
formattedCSV.close()
csvfile.close()

#reopen csvfile with read permissions for pandas
csvfile = open('fb_daily.csv', 'r+')
df = pd.read_csv('fb_daily.csv')

df = df.sort_values('timestamp')

print(df.head())


# First calculate the mid prices from the highest and lowest
high_prices = df['high'].to_numpy()
low_prices = df['low'].to_numpy()
mid_prices = (high_prices+low_prices)/2.0

print(mid_prices.shape)

trainData = mid_prices[:1900]
testData = mid_prices[1900:]

print(testData.shape)

scaler = sklearn.preprocessing.MinMaxScaler()
train_data = train_data.reshape(-1,1)
test_data = test_data.reshape(-1,1)
