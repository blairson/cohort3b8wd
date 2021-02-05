first = int (input("How many sweets did the first person bring? "))
second = int (input("How many sweets did the second person bring? "))
third = int (input("How many sweets did the third person bring? "))

total = first + second + third

each = total // 3
remain = total % 3

message = f"Total number of sweets is {total}, each person gets {each} sweets, and {remain} sweets will remain."
print (message)