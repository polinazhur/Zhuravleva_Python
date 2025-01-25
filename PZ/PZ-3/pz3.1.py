# Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел
# A и B нечетное».

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

if A%2 and B%2:
    print("Каждое из чисел A и B нечетное")
else:
    print("Одно или два из чисел A и B четное")
