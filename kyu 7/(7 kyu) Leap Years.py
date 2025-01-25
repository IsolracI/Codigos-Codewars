# más cableado que la verga, pero no se me ocurrió ninguna lógica matemática pa' esto :p
def is_leap_year(year):
    if year < 400:
        if year % 100 != 0 and year % 4 == 0:
            return True
        if year % 100 == 0:
            return False
    
    if year > 400:
        if year % 400 == 0:
            return True
        else:
            result = year % 400
            if result % 100 != 0:
                if result % 4 == 0:
                    return True
                else:
                    return False
            else:
                return False

# respuestas de los demás

#1
def is_leap_year_v1(year):
    return (year % 100 and not year % 4) or not year % 400

isLeapYear = is_leap_year



#2
def is_leap_year(year):
    return True if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else False



#3
import calendar
def is_leap_year(year):
    return calendar.isleap(year) #tremendo cabrón xD



#4
def is_leap_year(year):
    return year%4 ==0 and year%100!=0 or year%400==0