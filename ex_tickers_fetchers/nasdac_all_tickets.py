import pandas as pd

table = pd.read_html('https://en.wikipedia.org/wiki/NASDAQ-100#Components')
df = table[4]  # В данном случае список тикеров находится в четвертой таблице на странице
tickers = df['Ticker'].tolist()
print(tickers)

tickers_string = ', '.join(tickers)
with open('tickers_nasdaq.txt', 'a') as f:
    f.write(tickers_string + '\n')