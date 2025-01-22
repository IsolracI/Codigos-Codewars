# yeah baby 7w7
def convert_palindromes_v2(numbers):
    new_list = []
    amount_of_numbers = len(numbers)
    pointer = 0
    while pointer < amount_of_numbers:
        selected_number = str(numbers[pointer])
        if selected_number == selected_number[::-1]:
            new_list.append(1)
        else:
            new_list.append(0)
        pointer = pointer +1
    return new_list

print(convert_palindromes_v2([101, 2, 85, 33, 14014]))



#v1 doesn't work
def convert_palindromes_v1(numbers):
    new_list = []
    for item in numbers:
        if item == item[::-1]:
            new_list.append(1)
        else:
            new_list.append(0)

# fixed v1 (you can't put the indexing inside de str command)
def convert_palindromes_v1(numbers):
    new_list = []
    for item in numbers:
        if str(item) == str(item)[::-1]:
            new_list.append(1)
        else:
            new_list.append(0)
    return new_list

print(convert_palindromes_v1([101, 2, 85, 33, 14014]))



# respuestas de los demás

#1
def ispalindrom(n):
    return 1 if str(n) == str(n)[::-1] else 0

def convert_palindromes(numbers):
    return [ispalindrom(x) for x in numbers]



#2
def convert_palindromes_v3(numbers):
    return [str(n)==str(n)[::-1] for n in numbers]

print(convert_palindromes_v3([101, 2, 85, 33, 14014]))