# multiplication table
multiple = 2
multiplier = 1
max_multiplier = 13

while multiplier < max_multiplier:
    print (f"{multiple} x {multiplier}".ljust(10), "|",multiplier * multiple  )
    multiplier += 1
    

# # long multiplication
# for i in range (1,12):
#     for n in range (1,12):
#         print (f"{n*1}".center (6), "|", end = "")
#     print ()
#     if i ==1:
#         print ("_" * 20)


# loan schedule 

p = int (input ("please ENTER THE VALUE OF P:" ))
r = int (input ("please ENTER THE VALUE OF R:" ))
t = int (input ("please ENTER THE VALUE OF T:" ))

number_of_payment = 0 
while number_of_payment < t:
    payment = (p + (p*r*t))/100))/t
    print (f"month {number_of_payment+1} "|", payment )
    number_of_payment +=1
