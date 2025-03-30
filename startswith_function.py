#Prog05. startswith() check if the string beginning part matches the function parameter.
#Create a program that do the same functionality without using startswith() function.

#ask user for a string and the letter to check if that is in the beginning

user_string = input("Please enter a string: ")

start_letter = input("startswith() please enter a character: ")

#reverse both strings and use endswith function

if user_string[::-1].endswith(start_letter[::-1]) == True:
    print(True)
else:
    print(False)