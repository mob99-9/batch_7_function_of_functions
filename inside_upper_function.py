#Prog03. upper() converts all characters of the string into upper case.
#Create a program that do the same functionality without using upper() function

#ask user for a string

user_string = input("Please enter a string: ")

#turn the string into a list

user_list = list(user_string)

#create an empty string for the upper cased string

new_string = ""

#capitalize every character in the list and add to the new string

for character in user_list:
    new_string += character.capitalize()

#print the new string

print(new_string)