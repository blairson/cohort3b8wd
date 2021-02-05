# write a program that takes a name and last name seperated by comma and write the first name into
# a file named the last name

firstname = input("enter your first name: ")
lastname = input("enter your last name: ")

file = open(f"./devjoseph/{lastname}.txt", "w")
file.write(firstname)