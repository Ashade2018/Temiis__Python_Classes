#def is used to indicate a function followed by the function name, a parenthesis and a colon
from unicodedata import name


def say_hi(name, age):
    #the code in a function is indented, it has a paragraph
    print("Hello "+ name+ "YOu are "+ str(age)) 
#name in lowercase or add an underscore between two words
#a parameter is a piece of information we give to ther function
say_hi("Mike", 35)
#it's best to break your code intodifferednt functions