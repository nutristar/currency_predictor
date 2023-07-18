# Открываем файл в режиме чтения
# 'tickers_snp500.txt'
def extracter_from_text(file):
    with open(file, 'r') as f:
        # Читаем первую строку файла
        first_line = f.readline().strip()  # Метод strip() удаляет пробелы и переводы строк с концов строки

    # Разделяем строку по запятым, чтобы получить список тикеров
    tickers = first_line.split(',')

    # Убираем пробелы в начале и конце каждого тикера и оборачиваем тикер в кавычки
    tickers = ['{}'.format(ticker.strip()) for ticker in tickers]

    return tickers
s500_list=extracter_from_text('tickers_snp500.txt')
nasdaq_list=extracter_from_text('tickers_nasdaq.txt')
common_list=s500_list+nasdaq_list
print(common_list)
print(len(common_list))
common_list=list(set(common_list))
print(len(common_list))