#lists are invaluable in python
#popular functions in lists
#1. extend function: You can add another list to your initial list.
#2. append fxn: adds an additional item to a list
#3. insert fxn; takes two parametrs. the position you want it to be and the name you want to include
#4 remove fxn: removes the element you want from the list
#5. reset fxn
#6. pop: pops an item from the list i.e the last element.
#7. sort in alphabetical order
#8.
lucky_numbers = [24, 5, 13, 8, 20]
friends = ["John", "Doe", "sally", "Tobias"]
friends[3]= "Mike"
friends.append("Dave")
friends.extend(["Mabel", "Dipper", "Stan"])
print(len(friends))
lucky_numbers.sort()
#print(type(friends))
#lucky_numbers.append(28)
#print(lucky_numbers)
print(lucky_numbers.index(13))
#print(lucky_numbers)
#friends.sort()
friends.remove("John")
friends.append("Tobias")
print(friends)
animals = ["elephant", "lion", "tiger", "giraffe", "monkey", "dog"]  # Create a new list
print(animals)

animals[1:3] = ["cat"]    # Replace 2 items -- "lion" and "tiger" with one item -- "cat"
print(animals)

animals[1:3] = []     # Remove 2 items -- "cat" and "giraffe" from the list
print(animals)

animals[1:]=[]

print(animals.index("elephant"))
