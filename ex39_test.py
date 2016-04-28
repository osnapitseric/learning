import hashmap

states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

print(" - " * 10)
print("ny state has {}".format(hashmap.get(cities, "NY")))
print("or state has {}".format(hashmap.get(cities, "OR")))

print(" - " * 10)
print("michigan's abbreviation is: {}".format(hashmap.get(states, "Michigan")))
print("florida's abbreviation is: {}".format(hashmap.get(states, "Florida")))

print(" - " * 10)
print("michigan has: {}".format(hashmap.get(cities, "Michigan")))
print("florida has: {}".format(hashmap.get(cities, "Florida")))

print(" - " * 10)
hashmap.list(states)

print(" - " * 10)
hashmap.list(cities)

print(" - " * 10)
state = hashmap.get(states, "Texas")
if not state:
    print("Sorry, no Texas")

city = hashmap.get(cities, "TX")
print("the city for the state TX is: {}".format(city))

print(states)
