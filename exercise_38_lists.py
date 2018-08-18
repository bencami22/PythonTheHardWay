ten_things="Apples Oranges Crows Telephon Light Sugar"

print('Wait there are not 10 things in that list, lets fix that')

stuff=ten_things.split(' ')
more_stuff=["Day", "Grass", "Keyboard", "Sunglasses", "Table", "Truck", "Banana"]

while len(stuff)!=10:
    next_one=more_stuff.pop()
    print("Adding: ",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} in the list now")

print("There we go: ", stuff)

print("Lets do some things with stuff")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
