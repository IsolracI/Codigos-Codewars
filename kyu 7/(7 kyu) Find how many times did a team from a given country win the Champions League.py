# heck yeah!!
def count_wins(winners_list, country):
    num_of_victories = 0

    for league in winners_list:
        if country in league.values():
            num_of_victories += 1

    return num_of_victories

# respuestas de los demás

#1
def countWins(winners, country):
    return str(winners).count(country)