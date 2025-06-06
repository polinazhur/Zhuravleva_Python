# В матрице элементы последней строки заменить на 0.

matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15, 16]
]

matrix.pop()
matrix.append([0 for i in range(len(matrix[0]))])
print(matrix)