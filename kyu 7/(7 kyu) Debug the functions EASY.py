import math

def multi(l_st):
    multiplied_list = math.prod(l_st)
    return multiplied_list

def add(l_st):
    summed_list = sum(l_st)
    return summed_list

def reverse(st):
    reversed_string = st[::-1]
    return reversed_string

print(multi([8,2,5]))





# ejemplos de respuestas


def multi_v1(l_st):
    count = 1
    for i in l_st:
        count *= i
    return count

def add(l_st):
    count = 0
    for x in l_st:
        count += x
    return count

