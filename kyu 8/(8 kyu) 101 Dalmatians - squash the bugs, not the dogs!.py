def how_many_dalmatians(number):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    if number <= 10:
        respond = dogs[0]
    if number > 10 and number <= 50:
        respond = dogs[1]
    if number > 50 and number <= 100:
        respond = dogs[2]
    if number == 101:
        respond = dogs[3]
    return respond


# Other answers from codewars
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    return dogs[0] if n <= 10 else dogs[1] if n <=50 else dogs[3] if n == 101 else dogs[2]



def how_many_dalmatians(n):
  dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
  
  if n <= 10:
      return dogs[0]
  elif n <= 50:
      return dogs[1]
  elif n < 101:
      return dogs[2] 
  else:
      return dogs[3]



def how_many_dalmatians(n):
  dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
  if n <= 10: return dogs[0] 
  if n <= 50: return dogs[1] 
  if n == 101: return dogs[3]
  return dogs[2]



DOGS = ((100, '101 DALMATIONS!!!'), (50, 'Woah that\'s a lot of dogs!'),
        (10, 'More than a handful!'))

def how_many_dalmatians(n):
    return next((msg for dogs, msg in DOGS if n > dogs), 'Hardly any')