#Conditional Statements

#Try split on a string
# raise ValueError("Input must be whole number")   #print("Input must be whole")

sweets = int(input ("Please input total number of sweets available: "))
while True:
    try:
    
        ade = sweets%3
        quot = sweets // 3
    except:
        print ("You have to input a whole number.")


print (f"The three friends will get {quot} sweets each and {ade} sweet(s) will remain.")








