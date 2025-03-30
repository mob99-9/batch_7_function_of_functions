
#Prog01. rstrip() remove the space characters at the end of the string. 
#Create a program that do the same functionality without using rstrip() function.

#ask user for a string

user_string = input("Please input a string: ")

#create an empty string 

new_string = ""

#add the spaces from the right until the first non-space character

for char in user_string:
    if char == " ":
        new_string += char
    else:
        break

#add the non-space characters 

new_string += user_string.strip()

#print the new string

print(new_string) 