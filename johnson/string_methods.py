# name = "Ade"

# print(name.lower()) 
# print(name.upper()) 

# error_text = "     adekunbi  "

# print(error_text, name)
# print(error_text.strip(), name) # .strip() removes leading and trailing spaces from text

# file = open("mydata.txt", "r")
# data = file.read()

# print(data)
# print()
# print(data.replace("a boy", "Selim")) # replace values in a text.

# date_of_birth = "02/03/2021"
# print(date_of_birth.split("/")) # split divides a text into parts using a delimiter or value seperating the items to be splitted i.e (/) in this case

# print("Day : ", date_of_birth.split("/")[0])
# print("Month : ", date_of_birth.split("/")[1])
# print("Year : ", date_of_birth.split("/")[2])

# tran_id = "uba:12209-20000"

# in case of multiple splits one might break the process down into steps and split one after the other.
# first_split = tran_id.split(":")
# print(first_split)
# numeric_part = first_split[1]
# numbers = numeric_part.split("-")
# print(numbers)

# print("Val1: ", first_split[0])
# print("Val2: ", numbers[0])
# print("Val3: ", numbers[1])

# mynames = ["1", "2", "3"] 

# print("-".join(mynames)) # join takes a delimiter and uses it to join up values in a list.

# print("WELCOME THIS PROGRAM CHECKS IF A WORD STARTS WITH LETTER (A).")

# # word = input("Please enter a word : ")
# # print(word.startswith("a")) # starts with checks that a word starts with a given character. Note that it is case sensitive

# # word = input("Enter text : ")
# # normalized_version_of_word = word.lower() # this is assuming that we are using lower case as the standard metric for our application

# # print(normalized_version_of_word.endswith("ot"))

# word = "international"

# print(word.find("l"))


# age = input("Please enter your age: ")
# month = input("Please enter your month: ")
# day = input("Please enter your day o'birth: ")

# current_year = 2021
# year_of_birth = current_year - int(age) # any time values are collected from terminal they are automatically recieved in string format. Hence to deal with numeric variables one must convert to number using either the (float) or (int) builtin functions

# date_of_birth = str(year_of_birth) + "-" + str(month) + "-" + str(day) # STRING CONCATENATION

# print(date_of_birth)

# print(not bool(10%2)) # returns the remainder after a division

# print(23/4)
# print(23//4) # FLOOR DIVISION - REMOVES EVERYTHING AFTER THE DECIMAL PLACE.

# p = float(input("Please enter a value for P : "))
# r = float(input("Please enter a value for R : "))
# t = float(input("Please enter a value for T : "))

# i = (p*r*t)/100

# message = "If you take a loan of " + str(p) + " at the rate of " + str(r) + " for a period of " + str(t) + "months you will pay back " + str(i) + " as interest"

# print(message)

# message = f"If you take a loan of {p:,} at the rate of {r}% for a period of {t}months you will pay back {i:,} as interest" # to add comma between numbers i.e 1,100,900 use curly braces with colon and comma i.e {int_var:,}

# print(message)

# += assignment op add and reassign

# x = 2
# print(x)
# x+=1
# print(x)
# x+=2
# print(x) 

# logical opps

# x = True
# y = False
# z = True

# print(x or y)
# print(x and y)
# print(y and x or z)

# name = "alade"
# print("a" not in name)



# age = input("please how old are you :")
# day = input("which day were you born :")
# month = input("please state the month :")
# print(age)


# x = ("a+b")
# b = ("c+5")
# a = 3
# c = 4

# print (x)

#FIRST METHOD
# import cmath
# print("General Form:- ax**2 + bx + c=0")

# a = int(input("Enter a !=0"))
# b = int(input("Enter b:"))
# c = int(input("Enter c:"))
# disc = b**2 - 4*a*c
# sol1 = (-b-cmath.sqrt(disc))/(2*a)
# sol2 = (-b+cmath.sqrt(disc))/(2*a)
# # print(sol1,sol2)


# print("this is to find the root of the quadratic equation")
# a = int(input("enter the first coefficient of the equation"))
# b = int(input("enter the second coefficient of the equation"))
# c = int(input("enter the third coefficient of the equation"))
# from math import sqrt
# disc = b**2 - 4*a*c
# disc1 = sqrt(disc)
# positive = (-b + disc1)/(2*a)
# negative =(-b - disc1)/(2*a)
# print(positive,negative)


# print("this is to find the value of a,b and c in the equation")
# a = int(input("enter the value of a in the equation"))
# b = int(input("enter the value of b in the equation"))
# c = int(input("enter the value of c in the equation"))
# hyp = a**2
# adj = b**2
# opp = c**2
# disc1 = adj + disc3
# print(disc1)
# disc2 = disc1 + disc3
# print(disc2)
# disc3 = disc1 + disc2
# print(disc3)


# print("this is to find the root of the quadratic equation")
# a = int(input("enter the first coefficient of the equation"))
# b = int(input("enter the second coefficient of the equation"))
# c = int(input("enter the third coefficient of the equation"))
# from math import sqrt
# disc = b**2 - 4*a*c
# disc1 = sqrt(disc)
# positive = (-b + disc1)/(2*a)
# negative =(-b - disc1)/(2*a)
# print(positive,negative)



# print("this is to find the value of a,b and c in the equation")
# a = int(input("enter the value of a in the equation"))
# b = int(input("enter the value of b in the equation"))
# c = int(input("enter the value of c in the equation"))
# hyp = a**2
# adj = b**2
# opp = c**2
# hyp = adj + opp
# print(hyp)
# adj = hyp + opp
# print(adj)
# opp = hyp + adj
# print(opp)

# x = "c"
# print(x)
# print(not x)


# print("Write a program that takes a string and print the reverse")
# s = input("Please enter some strings")
# L = s.split()
# L1 = L[ : : -1]
# Y = " ".join(L1)
# print(Y)


# print("Write a program to test if a word is a palindrome")
# S = input("Please can you enter a word? :")
# print(S [ : :])
# revstr = (S[ : : -1])
# if revstr == S :
#     print("palindrome")
# else :
#         print("Not palindrome")



# print("Write a program take an integer and prints its as power of the integer")
# S = int 
# X = int
# S = int(input("put the value of S"))
# X = int(input("put the value of X"))
# Y = S**X
# print(Y)


print("Write a program take an integer and prints its as power of the integer")
X = int
X = int(input("put the value of X - "))
print(X**2, X**3, X**4)
print(X,X*X,X**X)
print(f'X,X*X,X**X')














    