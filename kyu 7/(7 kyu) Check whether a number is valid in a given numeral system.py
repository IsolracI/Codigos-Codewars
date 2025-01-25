# :3
def validate_base(num, base):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sorted_nums = sorted(num)
    biggest_value = sorted_nums.pop()

    if biggest_value in list(alphabet):
        biggest_value = alphabet.find(biggest_value) + 10
    
    return int(biggest_value) < base

# respuestas hechas por los demás

#1 
def validate_base_v1(num, base):
    return all([n in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base] for n in num])



#2
def validate_base_v2(num, base):
    try:
        num = int(num, base)
        return True
    except:
        return False



#3
def validate_base_v3(num, base):
    for char in num:
        if char.isdigit():  # If the character is a digit (0-9)
            value = int(char)
        elif char.isalpha():  # If the character is a letter (A-Z)
            value = ord(char) - ord('A') + 10  # Convert A-Z to 10-35
        else:
            return False  # Invalid character
        
        if value >= base:  # If the value exceeds the base
            return False
    
    return True