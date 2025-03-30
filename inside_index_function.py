#Prog09. index() return the first location of the function parameter in the string.
# Create a program that do the same functionality without using index() function.

# ask user for a string and a character to search 

user_string = input("Please input a string: ")

character = input("What will be searched from the string: ")

location = 0

#use find function 

location = user_string.find(character)

# if character not in user string, print error

if location == -1:
    location = "Error"

else:
    None
# print location

print(location)