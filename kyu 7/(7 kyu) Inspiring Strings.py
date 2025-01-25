# YIIIIEEEEEEAAAAHH BEIBEEEEEEEEEEEE!!!! (this one was kindda quick xD)
def longest_word(string_of_words):
    list_of_words = string_of_words.split(" ")
    longest_word = ""

    for word in list_of_words:
        if len(word) >= len(longest_word):
            longest_word = word
    return longest_word


# respuestas de los demás

#1
def longest_word_v1(string_of_words):
    return max(reversed(string_of_words.split()), key=len)