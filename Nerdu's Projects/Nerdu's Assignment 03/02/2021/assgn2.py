#Palindrome Test
panword = input ("Please enter test word: ")
panwordrev = "".join(reversed(panword))
print (f"Is your word a palindrome? {panword == panwordrev}")