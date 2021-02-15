# multiplication table
# multiple = 2
# multiplier = 1
# max_multiplier = 13

# while multiplier < max_multiplier:
#     print (f"{multiple}x{multiplier}".ljust(5), "|", multiplier * multiple)
#     multiplier += 1
    

# # long multiplication
# for i in range (1,12):
#     for n in range (1,7):
#         print (f"{n*1}".center (6), "|", end = "")
#     print ()
#     if i ==1:
#         print ("--" * 30)


# loan schedule 

# p = int (input ("please ENTER THE VALUE OF P:" ))
# r = int (input ("please ENTER THE VALUE OF R:" ))
# t = int (input ("please ENTER THE VALUE OF T:" ))

# number_of_payment = 0 

# while number_of_payment < t:
#     payment = (p + ((p*r*t)/100))/ t
#     print (f"month {number_of_payment+1}" "|", payment)
#     number_of_payment +=1

# determine Even number from odd number

# even = []
# odd = []
# for n in range (1,100+1):
#     if n % 2 == 1:
#         even.append(n)
# #         print (even)
#     if n % 2 == 1:
#         odd.append (n)
#         print(odd)
#     print (f"[even]"[odd])
    

# num = int (input("Enter a number: "))

# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))

combs = [1,2,3,4,5,6,7,8,9]
combs[1:]
combs[2:6]
print(combs[-len(combs):])

