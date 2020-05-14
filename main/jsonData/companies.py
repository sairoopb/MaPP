# ==========================================================================
# Only for a given set of 10 companies the data is being extracted/collected
# to make predictions as they are independent and are also likely to sample
# lot of variation from engineering, beverages, mdicine, investment banking 
# etc and the corresponding ensembles are being used.
# ==========================================================================

selected = [
    'GS',
    # 'NKE',
    # 'MCD',
    # 'PFE',
    # 'DIS',
    # 'INTC',
    # 'WMT',
    # 'JNJ',
    # 'JPM',
    # 'AAPL'  
]

# ===================================
# Companies to be added in the future
# ===================================

all_companies_list = [
    'TRV',
    'DOW',
    'WBA',
    'CAT',
    'GS',
    'MMM',
    'AXP',
    'UTX',
    'IBM',
    'NKE',
    'MCD',
    'BA',
    'CSCO',
    'CVX',
    'PFE',
    'MRK',
    'VZ',
    'KO',
    'DIS',
    'HD',
    'XOM',
    'UNH',
    'INTC',
    'PG',
    'WMT',
    'JNJ',
    'JPM',
    'V',
    'AAPL',
    'MSFT'
]

# Companies List:
# 1.Travelers                 ==== TRV
# 2.Dow                       ==== DOW
# 3.Walgreens Boots Alliance  ==== WBA
# 4.Caterpillar               ==== CAT
# 5.Goldman Sachs             ==== GS
# 6.3M                        ==== MMM
# 7.American Express          ==== AXP
# 8.United Technologies       ==== UTX
# 9.IBM                       ==== IBM
#10.Nike                      ==== NKE
#11.McDonald's                ==== MCD
#12.Boeing                    ==== BA
#13.Cisco                     ==== CSCO
#14.Chevron                   ==== CVX
#15.Pfizer                    ==== PFE
#16.Merck & Co                ==== MRK
#17.Verizon                   ==== VZ
#18.The Coca-Cola Company     ==== KO
#19.Disney                    ==== DIS
#20.Home Depot                ==== HD
#21.Exxon Mobil               ==== XOM
#22.UnitedHealth Group        ==== UNH
#23.Intel                     ==== INTC
#24.Procter & Gamble          ==== PG
#25.Walmart                   ==== WMT
#26.Johnson & Johnson         ==== JNJ
#27.JPMorgan                  ==== JPM
#28.Visa                      ==== V
#29.Apple                     ==== AAPL
#30.Microsoft                 ==== MSFT