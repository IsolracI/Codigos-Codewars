# yeeeeeeeeeeeeeeeeeeeeeeeeeeeeah beibee!!!!!
def crossing_sum(matrix, row_num, col_num):
    numbers_to_sum = []

    numbers_to_sum.append(sum(matrix[row_num]))

    for row in matrix:
        if row != matrix[row_num]:
            numbers_to_sum.append(row[col_num])
    
    sumed_numbers = sum(numbers_to_sum)

    return sumed_numbers

# respuestas de los demas

#1
def crossing_sum(matrix, row, col):
    return sum(matrix[row]) + sum(line[col] for line in matrix) - matrix[row][col]