import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from textData import TextRetriever
from stockData import StockRetriever

import datetime as datetime
import csv as csv
import time

global_start = time.time()

START = '2017-01-09'
END = '2018-05-23'
PERIOD = 50
PREDICTION = 10
COUNT = 35 + PERIOD
COMPANY = 'GS'

text = TextRetriever()
stock = StockRetriever(start=START, end=END, period=PERIOD)

dates = stock.get_dates()

tData = []
stockVal = []
input_final = []
output_final = []
datapoints = 0

print("\n=============================================================================================================================\n")

for i in range(PERIOD, len(dates) - PREDICTION):
    if i > COUNT:
        start = time.time()
        temp = text.textData(dates[i])
        end = time.time()
        time_elapsed = (end - start)
        tData.append(temp)
        flag = True if temp != 'NULL' else False
        datapoints += 1 if flag else 0
        print(f'Text Data Retreival information ==> Iteration == [{(i - COUNT - 1):3d}] || Date == [{dates[i].date()}] || Found == [{flag!s:^5}] || Time Elapsed == [{time_elapsed:3.3f}]')
    else:
        tData.append("NULL")

print("\n=============================================================================================================================\n")

start = time.time()
val = stock.get_stock(COMPANY)
for i in range(PERIOD, len(dates) - PREDICTION):
    dateList = [dates[j] for j in range(i - PERIOD,i + 1)]
    stockVal.append(val.loc[dateList].values.round(3).tolist())
    input_final.append(val.loc[dates[i], ['Open', 'Low', 'High', 'Close']].values.round(3).tolist())
    datelist_pred = [dates[j] for j in range(i + 1, i + PREDICTION)]
    output_final.append(val.loc[datelist_pred, ['Open', 'Low', 'High', 'Close']].values.round(3).tolist())
end = time.time()
time_elapsed = (end - start)
print(f'Stock Data Retreival information ==> Company == [{COMPANY!s:^3}] || Time Elapsed == [{time_elapsed:3.3f}]')

print("\n=============================================================================================================================\n")

table = []

fields = ['Date', 'Review', 'Input Hidden', 'Input Final', 'Output']

for i in range(PERIOD, len(dates) - PREDICTION):
    temp = []
    j = i - PERIOD
    if tData[j] == 'NULL':
        continue
    temp.append(stockVal[j])
    temp.append(input_final[j])
    temp.append(output_final[j])
    temp.insert(0, tData[j])
    temp.insert(0, dates[i].date())
    table.append(temp)    

filename = 'Data_GS_2017_2018.csv'

with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(table)

global_end = time.time()

total_execution = global_end - global_start

print(f"Total time taken for execution == [{total_execution:5.2f}] || Total number of datapoints == [{datapoints}] \n")