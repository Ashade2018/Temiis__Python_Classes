#simulate the basic calculator function in a simple python program and obtain user input to perform the arithmetic operations.
#Test case 1:
#A function to calculate called : Simply_calc
# It takes in how many parameters: at keast two
# What does the function perform?
# It returns the operation right/
# It asks for  two inputs from the user of float type right
# the user inouts their values and the return statement returns the operation above 
# the funtion is called before printing the answer.//not so sure of the last step.
def simply_Calc(num1, num2):
    return(num1/num2)
    #num1= float(input("The first number is : \n"))
    #num2= float(input("The second  number is : \n"))
    
answer = simply_Calc (num1= float(input("The first number is : \n")),
    num2= float(input("The second  number is :\n")))
print( answer)