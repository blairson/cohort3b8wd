# definite_number = 3
# highest_number = 1

# while highest_number<= 12 :
#     multiplication_table = definite_number * highest_number
#     print (f"{definite_number} x {highest_number}" .ljust(7),"|", multiplication_table)
   
#     highest_number +=1

Loan_amount = int(input ("Enter Loan amount :"))
interest_rate = int(input ("Enter interest :"))
Duration = int (input ("Enter duration  :"))

number_of_payment = 0

while number_of_payment < Duration :
    interest_amount = Loan_amount *  (interest_rate*Duration)
    total_repayment = Loan_amount + interest_amount
    monthly_repayment = total_repayment/Duration


    print (f"month{number_of_payment+1} |", monthly_repayment)
    number_of_payment +=1

    
