def unique_in_order(sequence):
    unique_list = []
    
    for element in sequence:
        if not unique_list:
            unique_list.append(element)
        else:
            if unique_list[-1] != element:
                unique_list.append(element)
    return unique_list



# respuestas de los demás

#1
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char     #una manera más astuta de controlar ese primer caracter.
    return result
