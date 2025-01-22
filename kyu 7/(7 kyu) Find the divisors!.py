# YEES BIIITCH!!!
def divisors(integer):
    number = 2
    all_divisors = []
    while number < integer:
        result_division = integer % number
        if result_division == 0:
            all_divisors.append(number)
            number += 1
        else:
            number += 1
    if all_divisors:
        return all_divisors
    else:
        return f'{integer} is prime'
    
print(divisors(15))


# respuestas de los demás

# 1
def divisors(integer):
  a = []
  for i in range(2, integer):
    if integer % i == 0:
      a.append(i)
  return a if a else str(integer) + " is prime"

# 2
def divisors(integer):

    lst = []
    for i in range(2,integer):
        if integer % i == 0:
            lst.append(i)
            
    if len(lst) == 0:
        return "%s is prime" % (integer)
    else:
        return lst
    
# 3
def divisors(n):
  
  divs = set()
  
  for t in range(2, int(n ** 0.5) + 1):
    div, mod = divmod(n, t)
    
    if mod==0:
      divs.add(t)
      divs.add(div)
  
  return '{:d} is prime'.format(n) if len(divs)==0 else sorted(list(divs))