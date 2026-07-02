# dictionary comprehension = create dictionaries using an expression
# can replace for loops and certain lambda functions

# FORMULAS:-
# dictionary = {key : expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictioanry = {key: (if/else) for (key, values) in iterable}

cities_in_F = {"San Francisco" : 100, "Boston" : 75, "Los angeles" : 80, "chicago" : 50}

cities_in_C = {key : round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

print("--------------------------------------------------------------------------")

weather = {"San Francisco" : "cloudy", "Boston" : "sunny", "Los angeles" : "cloudy", "chicago" : "sunny"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print((sunny_weather))

print("--------------------------------------------------------------------------")


def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69>= value >= 40:
        return "WARM"
    else:
        return "COLD"
    

cities = {"San Francisco" : 100, "Boston" : 75, "Los angeles" : 80, "chicago" : 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)
