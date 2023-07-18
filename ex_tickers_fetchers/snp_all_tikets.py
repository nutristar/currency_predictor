import pandas as pd
import pandas_datareader as pdr

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
tickers = df['Symbol'].tolist()
print(tickers)
print(len(tickers))
tickers_string = ', '.join(tickers)
with open('tickers_snp500.txt', 'w') as f:
    f.write(tickers_string)