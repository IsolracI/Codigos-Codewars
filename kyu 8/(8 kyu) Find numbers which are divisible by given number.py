# well... i'm about to become rank 6 so it's not like completing this excites me :v
def divisible_by(numbers, divisor):
    divisible_numbers = []

    for number in numbers:
        if number % divisor == 0:
            divisible_numbers.append(number)
    
    return divisible_numbers

# respuestas de los demás

#1
def divisible_by(numbers, divisor):
    return [n for n in numbers if n%divisor==0]