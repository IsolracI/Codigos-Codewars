def to_jaden_case(string):
    words_list = []

    for word in string.split():
        jaden_cased_word = word[0].upper() + word[1:].lower()
        words_list.append(jaden_cased_word)

    return " ".join(words_list)

# respuestas de los demás

#1
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
