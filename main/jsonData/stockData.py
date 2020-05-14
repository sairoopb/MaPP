from pandas_datareader import data as pdr
from jsonData.techIndicators import TechIndicators
import pandas as pd

class StockRetriever():

    def __init__(self, period, start='2016-05-08', end='2020-05-08'):
        temp = pdr.get_data_yahoo("MSFT",start=start, end=end)
        self.dates = temp.index
        self.start = start
        self.end = end
        self.tech_indicator = TechIndicators(period)

    def get_dates(self):
        return self.dates

    def get_stock(self, company):
        data = pdr.get_data_yahoo(company, start=self.start, end=self.end)
        data = data[['Open', 'Close', 'Low', 'High', 'Volume']]
        indicators = self.tech_indicator.getData(data)
        data = pd.concat([data, indicators], axis=1)
        return data

#==============================================================================

    # import yfinance as yf
    # yf.pdr_override()
    # stock_data.reset_index().to_json(None, orient='index', date_format='iso')

#==============================================================================