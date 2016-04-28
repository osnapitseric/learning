ten_things = "apples oranges crows telephone light sugar"

print("wait there are not 10 things in that list. let's fix that.")

stuff = ten_things.split()
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print("there are {} items now".format(len(stuff)))

print("there we go: ", stuff)
print("lets do some things with stuff")
print(stuff)
print(stuff[1])
print(stuff[-1])
print(stuff.pop()) #.pop() removes the last value in the list and adds to the next list
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

