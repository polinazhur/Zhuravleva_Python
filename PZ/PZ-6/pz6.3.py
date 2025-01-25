# Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
# этого элемента и его соседей.

import random
n = input("Введите длинну случайного списка: ")
while type(n) != int:
    try:
        n = int(n)
    except:
        n = input("Введите длинну случайного списка: ")

lst = [int(random.randint(1, 100)) for i in range(n)]

new_lst = []

# Для первого элемента
new_lst.append((lst[0] + lst[1]) / 2)

# Для элементов между первым и последним
for i in range(1, len(lst) - 1):
    new_lst.append((lst[i - 1] + lst[i] + lst[i + 1]) / 3)

# Для последнего элемента
new_lst.append((lst[-2] + lst[-1]) / 2)

print("Новый список:", new_lst)
