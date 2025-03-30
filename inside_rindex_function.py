#Prog10. rindex() return the first location of the function parameter in the string starting from the last character.
# Create a program that do the same functionality without using rindex() function.

# ask user for a string and a character to search 

user_string = input("Please input a string: ")

character = input("What will be searched from the string: ")

location = 0

#use find(value, -1) function to start at the end 

location = user_string.find(character, -1)

# if character not in user string, print error

if location == -1:
    location = "Error"

else:
    None
# print location

print(location)