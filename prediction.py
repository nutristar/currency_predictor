import pandas as pd
from keras.models import load_model

# Подготавливаем тестовые данные
X_test = pd.read_csv(f"for_predictions_datas/XCH-USD-R.csv")
X_test = X_test.drop('avg_price', axis=1)
model = load_model('my_model.h5')
# Здесь я предполагаю, что X_test уже загружен и содержит те же столбцы, что и X_train
X_test_reshaped = X_test.values.reshape((X_test.shape[0], X_test.shape[1], 1))

# Предсказываем цены
predicted_prices = model.predict(X_test_reshaped)

# Выводим предсказанные цены
print(predicted_prices)


# denormalized_prices = predicted_prices * (max_value - min_value) + min_value

import matplotlib.pyplot as plt

# Предположим, что predicted_prices содержит предсказания модели:


# Для построения графика, нам нужно преобразовать этот список списков в одномерный список
predicted_prices_flat = [price for sublist in predicted_prices for price in sublist]

# Строим график
plt.plot(predicted_prices_flat)
plt.title('Predicted Prices')
plt.xlabel('Time')
plt.ylabel('Price')
plt.show()
