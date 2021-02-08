# write a program that takes a string value and print the reverse

# write a program to test if a word is a palindrome

# write a program that takes an integer and prints is a such "a",  "a x a", axaxa

# write a program that takes first name and last name seperated by comma and write the first name into a file and the lastname.

# SOLUTION 1
# input_value = input('Please enter a word: ')
# rev_input_value = input_value[::-1]
# print(f'{input_value.title()} is reversed as: {rev_input_value.title()}')



# SOLUTION 2
# input_value = input('Please enter a word: ')
# if input_value == input_value[::-1]:
#     print(f'{input_value.title()} is a Palindrome')
# else:
#     print(f'{input_value.title()}, is not a Palindrome')


# SOLUTION 3
# input_num = int(input('Please enter a word: '))
# print(input_num**2,input_num**3,input_num**4)


# SOLUTION 4
# first_name = input('Enter your first name: ')
# last_name = input('Enter your last name: ')
# print('\n)
# print(first_name.title(), last_name.title(), sep = ', ')
# print('\n)
# file = open(f'{last_name}.txt', 'w')
# file.write(first_name)
# file.close()
# print('\n)
# file = open('bukoye.txt', 'r')
# print(file.read().title())