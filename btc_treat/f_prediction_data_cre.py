import pandas as pd

def extractor_from2(each):


    data = pd.read_csv(f"{each}.csv")

    df = data.drop(columns=['Date', 'Dividends', 'Stock Splits', 'Volume'])
    # Calculate the mean of the specified columns and create a new column 'avg_price'
    df['avg_price'] = df[['Open', 'High', 'Low', 'Close']].mean(axis=1)

    # Drop the specified columns
    df = df.drop(columns=['Open', 'High', 'Low', 'Close'])
    # print(df.head())
    print(each)
    min_value = df['avg_price'].min()
    max_value = df['avg_price'].max()

    # Затем мы нормализуем столбец, вычитая минимальное значение и делая это на разницу между максимумом и минимумом
    df['avg_price'] = (df['avg_price'] - min_value) / (max_value - min_value)
    # Сохраняем DataFrame в CSV-файл
    df.to_csv(f'../for_predictions_datas/{each}-R.csv')




extractor_from2("BTC-USD")
extractor_from2("UST-USD")
extractor_from2("XCH-USD")