# Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из символов C.

N = input("Введите целое число N: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        N = input("Введите целое число N: ")

C = input("Введите символ C: ")

print(C * N)
