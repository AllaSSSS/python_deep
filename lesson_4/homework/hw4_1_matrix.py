# Напишите функцию для транспонирования матрицы

from random import randint

number_of_rows = randint(2, 6)
number_of_columns = randint(2, 6)

print(number_of_rows)
print(number_of_columns)


def create_matrix(rows, columns):
    matrix = [[randint(0, 100) for i in range(rows)] for j in range(columns)]
    return matrix


def transpose_matrix(matrix):
    transposed = list(zip(*matrix))
    return transposed


init_matrix = create_matrix(number_of_rows, number_of_columns)

print(init_matrix)
print(transpose_matrix(init_matrix))





