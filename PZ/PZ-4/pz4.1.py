# Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A
# до B включительно.

A = input("Введите целое число A: ")
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        A = input("Введите целое число A: ")

B = input("Введите целое число B: ")
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        B = input("Введите целое число B: ")

sum_squares = 0 # для хранения суммы

for i in range(A, B + 1):
    sum_squares += i ** 2 # Добавляем квадрат числа

print(sum_squares)
