# Единицы длины пронумерованы следующим образом: 1 — дециметр, 2 — километр,
# 3 — метр, 4 — миллиметр, 5 — сантиметр. Дан номер единицы длины (целое число
# в диапазоне 1-5) и длина отрезка в этих единицах (вещественное число). Найти
# длину отрезка в метрах.

unit_number = input("Введите число измерения: ")
while type(unit_number) != int:
    try:
        unit_number = int(unit_number)
    except:
        unit_number = input("Введите число измерения: ")

length = input("Введите длинну: ")
while type(length) != int:
    try:
        length = int(length)
    except:
        length = input("Введите длинну: ")

if unit_number == 1:
    meters = length * 0.1
elif unit_number == 2:
    meters = length * 1000
elif unit_number == 3:
    meters = length * 1
elif unit_number == 4:
    meters = length * 0.001
elif unit_number == 5:
    meters = length * 0.01
else:
    meters = "Хмм... Что-то не так"

print(meters)
