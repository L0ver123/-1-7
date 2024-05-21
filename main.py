def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def find_max_in_column(matrix, k):
    max_value = float('-inf')
    max_index = -1
    for i in range(len(matrix)):
        if matrix[i][k] > max_value:
            max_value = matrix[i][k]
            max_index = i
    return max_value, max_index

def sum_negative_elements(row):
    return sum(x for x in row if x < 0) 

# Основная логика программы
file_path = '1.txt'
matrix = read_matrix_from_file(file_path)

k = int(input("Введите номер столбца k (начиная с 0): "))

max_value, max_index = find_max_in_column(matrix, k)

print(f"Максимальный элемент в {k}-м столбце: {max_value}")

row_with_max = matrix[max_index]
sum_negative = sum_negative_elements(row_with_max)

print(f"Сумма отрицательных элементов в строке с максимальным элементом: {sum_negative}")
