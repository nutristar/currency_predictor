import pandas as pd
from keras.models import load_model
import matplotlib.pyplot as plt
import json


def prediction(each):
    # Подготавливаем тестовые данные
    X_test = pd.read_csv(f"for_predictions_datas/{each}-R.csv")
    X_test = X_test.drop('avg_price', axis=1)
    model = load_model('my_model.h5')
    # Здесь я предполагаю, что X_test уже загружен и содержит те же столбцы, что и X_train
    X_test_reshaped = X_test.values.reshape((X_test.shape[0], X_test.shape[1], 1))
    # Предсказываем цены
    predicted_prices = model.predict(X_test_reshaped)
    # Выводим предсказанные цены


    # Затем мы можем считать данные из файла
    with open('btc_treat/values.json', 'r') as f:
        json_data2 = f.read()

    # Преобразуем строку JSON обратно в словарь
    data2 = json.loads(json_data2)

    # Извлекаем переменные из словаря
    min_value = data2[f'{each}min_value']
    max_value = data2[f'{each}max_value']
    print(min_value, max_value)

    denormalized_prices = predicted_prices * (max_value - min_value) + min_value

    print(denormalized_prices)
    # Для построения графика, нам нужно преобразовать этот список списков в одномерный список
    denormalized_prices = [price for sublist in denormalized_prices for price in sublist]
    # Строим график
    plt.plot(denormalized_prices)
    plt.title('Predicted Prices')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.show()


prediction("BTC")
