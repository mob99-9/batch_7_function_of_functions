#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. 
#Create a program that do the same functionality without using zfill() function.

#ask user for a number and ask how many digits it must have

user_number = int(input("Please enter an integer: "))

zero = int(input("How many digits it must have?: "))

#turn the number into a str and find lenght to subtract to the lenght of zeros

user_number = str(user_number)

number = zero - len(user_number)

#print the combination of the string of zero multiplied by the number and the user number

print("0" * number + user_number)