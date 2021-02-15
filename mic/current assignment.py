# ASSIGNMENT

# a = int (input ("enter number? : "))
# b = int (input ("enter number? : "))
# print (f"{a} is greater than {b}: {a > b}")
# print (f"{b} is greater than {a}: {b > a}")

# A = int (input ("enter the value of A: "))
# VALUE_A = A , A * A, A ** A
# print (VALUE_A)

# A = int (input ("enter the value of A: "))
# print ( A ,+ A * A , + A ** A)
# # # Palindrome

# word= input ("write a word: ")
# if(word == word [::-1]):
#     print ("the word is palindrome")
# else:
#     print ("not a palindrome")

# # print string
# def my_function(xyz):
#      return xyz[::-1]
# xyz= my_function("HELLO MY UNIVELCITY PEOPLE")
# print (xyz)

firstname = input("my first name : ")
lastname = input("my last name : ")
file = open(f"{lastname}.txt", "w")
file.write(firstname)
print("I've created your txt file")

a = int (input ("ENTER THE VAUES OF A ?  "))
print (a,+ a * a,+ a ** a)


#  # long multiplication
# for i in range (1,12):
#     for n in range (1,12):
#         print (f"{n*1}".center (6), "|", end = "")
#     print ()
#     if i ==1:
#         print ("_" * 20)