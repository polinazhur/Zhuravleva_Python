# Составить программу, в которой функцию построит изображение, в котором в
# первой строке 1 звездочка, во второй - 2, в третьей -3, ..., в строке с номером m - m
# звездочек.

def print_stars(m):
    for i in range(1, m + 1):  # От 1 до m
        print('*' * i)

A = input("Введите количество строк: ")
while type(A) != int:
    try:
        A = int(A)
    except:
        A = input("Введите количество строк: ")
print_stars(A)
