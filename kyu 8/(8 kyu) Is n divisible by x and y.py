def is_divisible(number, divisor1, divisor2):
    divisors = [divisor1, divisor2]

    for divisor in divisors:
        if number % divisor != 0:
            return False
    return True