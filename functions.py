#def is used to indicate a function followed by the function name, a parenthesis and a colon


def say_hi(name, age):
    #the code in a function is indented, it has a paragraph
    print("Hello "+ name+ " You are "+ str(age)) 
#name in lowercase or add an underscore between two words
#a parameter is a piece of information we give to ther function
say_hi("Mike", 35)
#it's best to break your code into different functions
#default parameters
# you can define functions in three ways.
#what is the print(f")
# the first way is to specify a default value for one or more arguments
# The f or F in front of strings tells Python to look at the values inside {} and substitute them with the values of the variables if exist.

agent = 'James Bond'
num = 9

# old ways
print('{0} has {1} number '.format(agent, num))

# f-strings way
print(f'{agent} has {num} number')#