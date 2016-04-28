states = {
    "oregon": "or",
    "florida": "fl",
    "california": "ca",
    "new york": "ny",
    "michigan": "mi",
}

cities = {
    "ca": "san francisco",
    "mi": "detroit",
    "fl": "jacksonville",
}

cities["ny"] = "new york"
cities["or"] = "portland"

print(" - " * 10)
print("michigan's abbreviation is: ", states["michigan"])
print("florida's abbreviation is: ", states["florida"])

print(" - " * 10)
for state, abbrev in states.items():
    print("{} is abbreviated {}".format(state, abbrev))

print(" - " * 10)
for state, abbrev, in states.items():
    print("{} state is abbbreviated {} and has city {}".format(state, abbrev, cities[abbrev]))
# dict also comes in two variables. cities[abbrev] connects the return (value in this case) of abbrev
# from states.items to match it with the key value in citites.

print(" - " * 10)
state = states.get("texas")
if not state:
    print("Sorry no such state in db")

city = cities.get("tx", "does not exist")
print("the city for the state 'tx' is: {}".format(city))

