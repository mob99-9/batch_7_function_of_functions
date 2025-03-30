#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. 
#Create a program that do the same functionality without using rjust() function.

#ask user for a string, spaces, and padding 

user_string = input("Please input a string: ")

spaces = input("How many spaces would you like?: ")

padding = " "

#make an rjust variable 

rjust = padding * int(spaces)

#add the rjust to the user string in the print function

print(rjust, user_string)