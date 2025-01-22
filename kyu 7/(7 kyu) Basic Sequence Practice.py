# thanks Rubi :3
def sum_of_n(n):
    initial_sequence = [0]
    initial_point = 0
    final_sequence = [0]
    while initial_point < abs(n):
        initial_point = initial_point + 1
        initial_sequence.append(initial_point)
        final_sequence.append(sum(initial_sequence))
    if abs(n) == n:
        return final_sequence
    else:
        negative_sequence = []
        for item in final_sequence:
            negative_sequence.append(-item)
        return negative_sequence

print(sum_of_n(-4))



# doesn't work IDK why
def sum_of_n(n):
    initial_sequence = [0]
    initial_point = 0
    final_sequence = [0]
    if abs(n) == n:
        while initial_point < n:
            initial_point = initial_point + 1
            initial_sequence.append(initial_point)
            final_sequence.append(sum(initial_sequence))
        return final_sequence
    else:
        while initial_point < n:
            initial_point = initial_point + 1
            initial_sequence.append(initial_point)
            number_to_add = sum(initial_sequence)
            final_sequence.append(-abs(number_to_add))
        return final_sequence



# respuestas de los demás

#1
def sum_of_n(n):
    return [(-1 if n < 0 else 1) * sum(xrange(i+1)) for i in xrange(abs(n)+1)]



#2
def sum_of_n(n):
    output = [0]
    sign = 1
    if n < 0: sign = -1
    for numb in range(1, abs(n) + 1):
        output.append(sign * (numb + abs(output[numb - 1])))
    return output


