from processing import filter_by_state, sort_by_date

# Пример входных данных
data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# 1. Фильтрация по статусу "EXECUTED" (по умолчанию)
executed_transactions = filter_by_state(data)
print("Транзакции со статусом EXECUTED:")
for item in executed_transactions:
    print(item)

# 2. Фильтрация по статусу "CANCELED"
canceled_transactions = filter_by_state(data, "CANCELED")
print("\nТранзакции со статусом CANCELED:")
for item in canceled_transactions:
    print(item)

# 3. Сортировка данных по дате (по убыванию)
sorted_data = sort_by_date(data)
print("\nДанные, отсортированные по дате (по убыванию):")
for item in sorted_data:
    print(item)
