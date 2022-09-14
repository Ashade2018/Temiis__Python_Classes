#a for loop is used to control instructionss.
# it is used for iteration and repetition
# iteration means performing the same operation on different items.
# e.g wash car,plates,clothes. that is whenever you see a car, you should wash it, or whenever you see a plate, you should wash it
# repetition means doing the same thing over and over. that is singing a song over and over or learning over and over.
# for example:#
students=["Ade", "Barry", "lily", "Jason", "nina"]
for d in students: #for loop syntax
    print(d)
#what happens is that for every item in the variable, print it out. it's a way of calling the things stored in a variable.
# d is known as the loop control variable or the iteration variable
# in keyword which is the connecting keyword follow by the name of the list you will like to loop over #
#an example where you can loop through and add a print statement to an item
# #
for d in students:
    print(d + " is my classmate")#iteration example, performing the same operation which is calling the items in the list.
#repition example: perform an operation more than once.
#e.g (range 10) will print a list from 0-9
#range is a function and is  is a quick and easy way to create a list of numbers with a start and end . 
#so let's create a tongue twister to be repeated 6 times#
for i in range(6):
    print(i)#this prints the iteration variable i in the range 0-5 for 6 times
    print("I scream, you scream, we scream, for ice cream")
print("Your turn!")
#it executes the code as long as it is in the block and is indented.
#what is a block of code?
# a block of code is a set of programming statements you want to group together.#
exampl = ["a","b","c","d"]
for i in exampl:
    print(i)
    for j in exampl: 
        print(j)
savings= 0
plates= 50
tyres= 120
bed= 100
spending= 30
for week in range(1,53):
    savings= savings+ plates+tyres+bed -spending
    print(week,"total= {}".format(savings))