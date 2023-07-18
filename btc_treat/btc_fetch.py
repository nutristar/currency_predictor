import yfinance as yf

try:
    # Используем тикер биткойна
    ticker = yf.Ticker('BTC-USD')

    # Получаем исторические данные
    hist = ticker.history(period="max")

    # Сохраняем данные в файл CSV
    hist.to_csv('BTC.csv')

except Exception as e:
    print(f"An error occurred: {e}")
