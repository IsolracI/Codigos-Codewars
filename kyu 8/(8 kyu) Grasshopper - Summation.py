# this one works.
def summation_v3(num):
    number_to_add = 1
    list_of_numbers = []

    if num == 1:
        return 1
    else:
        while number_to_add <= num:
            list_of_numbers.append(number_to_add)
            number_to_add = number_to_add + 1
            numbers_summed = sum(list_of_numbers)
        return numbers_summed

# doesn't work and IDK why. Made by me.
def summation_v1(num):
    number_to_add = 1
    if num == 1:
        return num
    else:
        while number_to_add < num:
            list_of_numbers = []
            print(list_of_numbers)
            list_of_numbers.append(number_to_add)
            print(list_of_numbers)
            number_to_add = number_to_add + 1
            print(number_to_add)
            numbers_summed = sum(list_of_numbers)
            print(list_of_numbers)
            return numbers_summed

# doesn't work and IDK why. Made by me.
def summation_v2(num):
    number_to_add = 1
    while number_to_add < num:
        list_of_numbers = []
        list_of_numbers.append(number_to_add)
        number_to_add = number_to_add + 1
        numbers_summed = sum(list_of_numbers)
        return numbers_summed







def summation(num):
    return sum(range(1,num+1))



def summation(num):
    return (1+num) * num / 2



def summation(num):
    total = 0
    for i in range(0, num+1):
        total = total + i
    return total