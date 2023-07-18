import pandas as pd
import os

import json


def to_json_saver(min_value, max_value, each):
    data = {}

    # Если файл существует, считываем данные из файла
    if os.path.exists('values.json'):
        with open('values.json', 'r') as f:
            data = json.load(f)

    # Добавляем новые данные
    data.update({
        f'{each}min_value': min_value,
        f'{each}max_value': max_value
    })

    # Записываем обновленные данные обратно в файл
    with open('values.json', 'w') as f:
        json.dump(data, f)





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
    to_json_saver(min_value, max_value, each)
    # Затем мы нормализуем столбец, вычитая минимальное значение и делая это на разницу между максимумом и минимумом
    df['avg_price'] = (df['avg_price'] - min_value) / (max_value - min_value)
    # Сохраняем DataFrame в CSV-файл
    # df.to_csv(f'../for_predictions_datas/{each}-R.csv')


extractor_from2("BTC")
extractor_from2("UST")
extractor_from2("XCH")
