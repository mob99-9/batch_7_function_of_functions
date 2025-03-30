#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter.
#Create a program that do the same functionality without using removesuffix() function.

#ask user for a string

user_string = input("Please input a string: ")

#ask the user what will be removed from the previous string

remove_character = input("What would be removed from the string: ")

#use rstrip function to remove the unwanted suffix

try:
    new_string = user_string.rstrip(remove_character)
    print (new_string)
except:
    print(f'{remove_character} is not at the end of {user_string}')