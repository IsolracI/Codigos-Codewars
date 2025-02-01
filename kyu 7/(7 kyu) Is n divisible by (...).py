def is_divisible(number, *args):
    for arg in args:
        if number % arg != 0:
            return False
    return True



def is_divisible(n, *args):
    return all(not n % i for i in args)