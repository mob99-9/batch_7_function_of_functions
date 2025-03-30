#Prog08. count() return how many time the function parameter appear in the string.
#Create a program that do the same functionality without using count() function.

#create an empty dictionary and ask user for a string

counter = {}

user_string = input("Please enter a string: ")

#count every character on the string and add it to the counter 

for char in user_string:
    if counter.get(char) == None:
        counter.update({char : 1})
    else:
        counter[char] += 1

#ask what will be counted and print it
count = input("What character would you like to count?: ")

print(counter[count])