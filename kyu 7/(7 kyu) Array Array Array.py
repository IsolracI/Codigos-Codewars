# cableado, pero es lo único que se me ocurrió
def explode1(arr):
    counter = 0
    new_array = []
    if str(arr[0]) != arr[0]:
        if str(arr[1]) != arr[1]:
            times_to_return = sum(arr)
            while counter < times_to_return:
                new_array.append(arr)
                counter = counter +1
            return new_array
        else:
            while counter < arr[0]:
                new_array.append(arr)
                counter = counter +1
            return new_array
    else:
        if str(arr[1]) != arr[1]:
            while counter < arr[1]:
                new_array.append(arr)
                counter = counter +1
            return new_array
        else: 
            return "Void!"


# respuestas de los demás

#1
def explode(arr):
    [a, b] = arr
    if isinstance(a, int) and isinstance(b, int):
        time = a + b
    elif isinstance(a, str) and isinstance(b, int):
        time = b
    elif isinstance(a, int) and isinstance(b, str):
        time = a
    else:
        return 'Void!'
    return [arr] * time



#2
def explode1(arr):  
    numbers = [n for n in arr if type(n) == int]
    return [arr] * sum(numbers) if numbers else "Void!"



#3
def explode(arr):
    return [arr] * sum(lst) if (lst:=[i for i in arr if isinstance(i, (int, float))]) else 'Void!'


