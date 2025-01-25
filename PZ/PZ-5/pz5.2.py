# Описать функцию AddLeftDigit(D, K), добавляющую к целому положительному
# числу K слева цифру D (D — входной параметр целого типа, лежащий в диапазоне
# 1-9, K — параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой функции последовательно добавить к данному числу K слева
# данные цифры D1 и D2, выводя результат каждого добавления.

def AddLeftDigit(D, K):
    # Добавляем цифру D слева к числу K
    K = int(str(D) + str(K))
    return K

K = input("Введите целое число K: ")
while type(K) != int:
    try:
        K = int(K)
    except ValueError:
        K = input("Введите целое число K: ")

D1 = input("Введите первую цифру D1 (1-9): ")
while type(D1) != int:
    try:
        D1 = int(D1)
        if D1 in range(1, 10):
            break
        else:
            D1 = input("Введите первую цифру D1 (1-9): ")
    except ValueError:
        D1 = input("Введите первую цифру D1 (1-9): ")

D2 = input("Введите вторую цифру D2 (1-9): ")
while type(D2) != int:
    try:
        D2 = int(D2)
        if D2 in range(1, 10):
            break
        else:
            D2 = input("Введите вторую цифру D2 (1-9): ")
    except ValueError:
        D2 = input("Введите вторую цифру D2 (1-9): ")

K = AddLeftDigit(D1, K)
print("После добавления D1:", K)

K = AddLeftDigit(D2, K)
print("После добавления D2:", K)
