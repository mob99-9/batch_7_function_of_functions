#Prog04. islower() check if all characters of the string is on lower case. 
#Create a program that do the same functionality without using islower() function.

#ask user for a string

user_string = input("Please input a string: ")

#create a islower variable and set it to False

islower = False

#check every character in the string with isupper() function

for char in user_string:
    if char.isupper() == False:
        islower = True
    else:
        islower = False
        break

#print islower variable

print(islower)