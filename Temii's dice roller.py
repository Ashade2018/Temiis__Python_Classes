#This is Temii's dice roller
# It is also a set of instructions I followed. Thank you
# Python is case sensitive
# indentation sensititive
#input(): The input function asks the user for an inpput 
# import random
# print("Hello World this is  a dice roller game")
# dice_input = int(input())
# dice_roll = random.randint(1, dice_input)
# #print(dice_roll)

    



#import random
#i need to import a random package to carry out a function
# the function is to take in random integers from 1-6#
#dice_numbers= random.randint(1,6)#returns random integers in ranges 1-6
#that is the condition set for looping
#i've set a varibale for that but when do i call it?
# whenever i need to roll my dice bah?
# ao while (i roll the dice, i can get a one , or a two, up to 6)#















#I am creating a dice rolling game and I need some variables.
#the first is a variable to store my dice_numbers that I can call on while it goes through an endless loop of being used.
# another is a variable that is used to store my choice to roll a dice or not, if yes, it answers the call to loop and if no, it ends it.
# the choice variable should ask me if i want to roll a dice or not.
# my_choice = input("would you like to roll a dice\n y/n")
# so, as it waits for my answer, it should start calling the dice_numbers with the endless loop and the one to end it
# endless loop call:
# while (my_choice == 'y'):
# dice_number=random.randint(1,6)
# that is the phone number for the call on speed dial. the no consists of a variable name to store dice numbers,
# a random package, with a module to take in a range from 1-6#
#if call = 1
# print("the shape for one dice roll")#
import random
print("This is Temiis dice rolling game!")
my_choice= input("Would you like to roll a dice?\n yes or no :")
while(my_choice=="yes"):
    dice_num = random.randint(1,7)
    if dice_num == 1: 
        print("""
         .............
         |           |
         |           |
         |     *     |
         |           |
         |           |
         ............."""),
    elif dice_num== 0:
     print()

    elif dice_num==2:
        print("""
         .............
         |           |
         |           |
         |    * *    |
         |           |
         |           |
         ............."""),
    elif dice_num==3:
         print("""
         .............
         |           |
         |           |
         |     *     |
         |    * *    |
         |           |
         ............."""),
    elif dice_num==4:
        print("""
         .............
         |           |
         |           |
         |    * *    |
         |    * *    |
         |           |
         .............""")
    elif dice_num==5:
         print("""
         .............
         |           |
         |    * *    |
         |     *     |
         |    * *    |
         |           |
         |           |
         .............""")
    elif dice_num==6:
         print("""
         .............
         |           |
         |           |
         |    * * *  |
         |    * * *  |
         |           |
         .............""")
    else: exit()


if(my_choice=="no"):
    exit()
