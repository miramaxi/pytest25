import random
mylist = ["apple", "banana", "cherry"]
print(random.choices(mylist, weights=[10, 1, 1], k=15))
# Метод choices() возвращает список со случайно выбранным элементом
#  из указанной последовательности. Последовательность может быть 
# строкой, диапазоном, списком, кортежем. Обрати внимание на пример.
# Здесь возвращается список из 15 элементов. Список содержит случайный 
# набор значений из указанного списка.
# Вероятность выбора “apple” в 10 раз выше, чем “banana” и “cherry”.