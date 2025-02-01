# el codigo más corto que he escrito hasta la fecha, i don't know how to feel about it 
def sum_two_smallest_numbers(numbers):
    return sorted(numbers).pop(0) + sorted(numbers).pop(1)

# respuestas de los demás

#1 
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

#2
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]