import talib as ta
import pandas as pd

# The technical indicators being used are as follows :
# 1.  Simple Moving Average (SMA)
# 2.  Exponential Moving Average (EMA)
# 3.  Moving average convergence/divergence (MACD)
# 4.  Stochastic (STOCH)
# 5.  Relative Strength Index (RSI)
# 6.  Average Directional Movement Index (ADX)
# 7.  Commodity Channel Index (CCI)
# 8.  Aroon (AROON)
# 9.  Bollinger Bands (BBANDS)
# 10. Chaikin A/D Line (AD)
# 11. On Balance Volume (OBV)
# 12. Average True Range (ATR)
# 13. Money Flow Index (MFI)
# 14. Parabolic SAR (SAR)
# 15. Standard Deviation (STDDEV)

# Note ==============================
# Taking the default close value for
# SMA, EMA, MACD, RSI, BBANDS, STDDEV
# ===================================

names = [
    'SMA',
    'EMA',
    'MACD',
    'STOCHK',
    'STOCHD',
    'RSI',
    'ADX',
    'CCI',
    'AROONU',
    'AROOND',
    'BBANDU',
    'BBANDD',
    'AD',
    'OBV',
    'ATR',
    'MFI',
    'SAR',
    'STDDEV'
]

class TechIndicators():

    def __init__(self, period):
        self.open = 'Open'
        self.close = 'Close'
        self.low = 'Low'
        self.high = 'High'
        self.vol = 'Volume'

        self.period = period

    def getData(self, data):
        col = []
        col.append(ta.SMA(data[self.close]))
        col.append(ta.EMA(data[self.close]))
        macd, _, _ = ta.MACD(data[self.close])
        col.append(macd)
        stochk, stochd = ta.STOCH(data[self.high], data[self.low], data[self.close])
        col.append(stochk)
        col.append(stochd)
        col.append(ta.RSI(data[self.close]))
        col.append(ta.ADX(data[self.high], data[self.low], data[self.close]))
        col.append(ta.CCI(data[self.high], data[self.low], data[self.close]))
        aroon_up, aroon_down = ta.AROON(data[self.high], data[self.low])
        col.append(aroon_up)
        col.append(aroon_down)
        bband_up, _, bband_down = ta.BBANDS(data[self.close])
        col.append(bband_up)
        col.append(bband_down)
        col.append(ta.AD(data[self.high], data[self.low], data[self.close], data[self.vol]))
        col.append(ta.OBV(data[self.close], data[self.vol]))
        col.append(ta.ATR(data[self.high], data[self.low], data[self.close]))
        col.append(ta.MFI(data[self.high], data[self.low], data[self.close], data[self.vol])) 
        col.append(ta.SAR(data[self.high], data[self.low]))
        col.append(ta.STDDEV(data[self.close]))

        final_data = []

        for column in col:
            final_data.append(pd.DataFrame(column))

        df = pd.concat(final_data, axis=1)
        df.columns = names
        return df