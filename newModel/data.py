import requests
import json
import csv
from pandas_datareader import data
import pandas as pd
#from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np

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

#Removed due to 32bit windows version of anaconda
#scaler = sklearn.preprocessing.MinMaxScaler()
trainData = trainData.reshape(-1,1)
testData = testData.reshape(-1,1)

"""
#Class that automates making of batches from csvData
class DataGeneratorSeq(object):

    def __init__(self,prices,batch_size,totBatches):
        self._prices = prices
        self._prices_length = len(self._prices) - totBatches
        self._batch_size = batch_size
        self._totBatches = totBatches
        self._segments = self._prices_length //self._batch_size
        self._cursor = [offset * self._segments for offset in range(self._batch_size)]

    def next_batch(self):

        batch_data = np.zeros((self._batch_size),dtype=np.float32)
        batch_labels = np.zeros((self._batch_size),dtype=np.float32)

        for b in range(self._batch_size):
            if self._cursor[b]+1>=self._prices_length:
                #self._cursor[b] = b * self._segments
                self._cursor[b] = np.random.randint(0,(b+1)*self._segments)

            batch_data[b] = self._prices[self._cursor[b]]
            batch_labels[b]= self._prices[self._cursor[b]+np.random.randint(0,5)]

            self._cursor[b] = (self._cursor[b]+1)%self._prices_length

        return batch_data,batch_labels

    def batches(self):

        unroll_data,unroll_labels = [],[]
        init_data, init_label = None,None
        for ui in range(self._totBatches):

            data, labels = self.next_batch()

            unroll_data.append(data)
            unroll_labels.append(labels)

        return unroll_data, unroll_labels

    def reset_indices(self):
        for b in range(self._batch_size):
            self._cursor[b] = np.random.randint(0,min((b+1)*self._segments,self._prices_length-1))



dg = DataGeneratorSeq(trainData,5,5)
u_data, u_labels = dg.batches()

for ui,(dat,lbl) in enumerate(zip(u_data,u_labels)):
    print('\n\Batch index %d'%ui)
    dat_ind = dat
    lbl_ind = lbl
    print('\tInputs: ',dat )
    print('\n\tOutput:',lbl)
"""
