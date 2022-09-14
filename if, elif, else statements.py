# # If Statements:
# # we learned that 'if' keyword is helpful whenever we need a condition to do either this or that. E.g take an umbrella or you be prepared to be drenched.
# # to declare an if statement, the syntax used is:
# # if(condition):
# # if is the 'if' keyword
# # condition: is created using a number of Boolean and conditional operators such as ==,!=,>=,<=, >,<. 
# # preceeding the colon: is a decision or process to be carried out. That process is defined, using a print function
# # Do this, or else?:
# # Otherwise, "you be prepared to be drenched", "you have failed the exam", "Errror", Those are examples of otherwise statements. To print your otherwise statement, we use an Else keyword. 
# # If.. Else
# # if (my_choice >=23):
# # 	print("you are above the age limit")
# # else: 
# # 	print("Welcome to the book club!")
# # notice, the indentation or spacing before the print statement. 
# #If..Elif.. Else
# my_choice=int(input("Please fill out your age!:"))
# if(my_choice >=23):
# 	print("You are not qualified for the job")
# elif(my_choice <10):
# 	print("You are underqualified for the job")
# elif (my_choice >=18 ): 
# 	print("You are fit for the job!")
# else:
#     print("Better luck next time")
x=int(input("Your age is:"))
score = 270
if (x>=16):
	print("You are an eligible candidate\n\n")
	if(score>=270):
		print("Congratulations! you have been given admission into your first choice")
	else: 
		print("Try again")
elif(x< 16):
	print("you are asked to withdraw")
elif(x==16):
	print("your age is accurate")
else: 
		print("Incorrect information")
