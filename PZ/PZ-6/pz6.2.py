# Дан список размера N. Найти количество участков, на которых его элементы
# монотонно возрастают.

import random
n = input("Введите длинну случайного списка: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        n = input("Введите длинну случайного списка: ")

lst = [int(random.randint(1, 100)) for i in range(n)]
print(lst)
# Переменная для подсчета количества участков
count = 0
n = len(lst)

# Проверка наличия хотя бы одного участка
if n > 0:
    in_increasing_segment = False

    for i in range(1, n):
        if lst[i] > lst[i - 1]:  # Если элемент больше предыдущего
            if not in_increasing_segment:
                count += 1  # Начинаем новый участок
                in_increasing_segment = True
        else:
            in_increasing_segment = False

print("Количество участков монотонно возрастающих чисел:", count)
