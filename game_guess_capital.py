############ Guess a Capital Game ############
"""
Use a dictionary to keep country-capital pairs as key-value.
Prompt the user 3 times for a capital in a country.
Print the number of correct capitals.
"""
import random

dict = {
    'France': 'Paris',
    'Poland': 'Warsaw',
    'Ukraine': 'Kiev',
    'Germany': 'Berlin',
    'Finland': 'Helsinki',
    'Sweden': 'Stockholm',
    'Denmark': 'Copenhagen',
    'Spain': 'Madrid',
    'Austria': 'Vienna',
    'Belgium': 'Brussels',
    'Czechia': 'Prague',
    'Italy': 'Rome'
}
countries = list(dict.keys())
country = ""
turns = 5
points = 0
print("We will test your knowledge of countries and their capitals.")

while turns > 0:
    turns -= 1
    country = random.choice(countries)
    user = input(f"What is a capitol of {country}? ")
    if user == dict[country]:
        print(f"You are correct. Capital of {country} is {dict[country]}")
        points += 1
    else:
        print(f"You are wrong. Capital of {country} is {dict[country]}")
print(f"You guessed {points} out of 5. Great job!")