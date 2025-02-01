def average_string(string):
    numbers_dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
                   "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    strings_dic = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                   5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    numbers_list = []

    if string:
        for word in string.split(" "):
            if word in numbers_dic:
                numbers_list.append(numbers_dic[word])
            else:
                return "n/a"
        
        average_number = sum(numbers_list) / len(numbers_list)
        return strings_dic[int(average_number)]

    else:
        return "n/a"