def weather_info_v1 (fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    if (celsius > 0):
        return (str(celsius) + " is freezing temperature")
    else:
        return (str(celsius) + " is above freezing temperature")
print(weather_info_v1(-19))



# Al definir weather_info ya le estás indicando dentro cual es la variable con la que convertToCelsius va a operar
def weather_info_v2 (temp):
    c = convertToCelsius(temp)
    if (c <= 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convertToCelsius (temperature):
    celsius = (temperature - 32) * (5.0/9.0)
    return celsius
print(weather_info_v2(50))