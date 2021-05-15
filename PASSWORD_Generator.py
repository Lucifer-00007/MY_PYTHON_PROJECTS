#Program to generate password with a random combination of UpperCase_Characters, LowerCase_Characters ,Numbers and Symbols.


# Type 1:
# import random

# # l=int(input("Enter the lenth of password ="))
# l=15

# # k=int(input("Enter the quantity of passwords ="))
# k=10


# DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
# 					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
# 					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
# 					'z']

# UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
# 					'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
# 					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
# 					'Z']

# SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']



# My_Combination=DIGITS+LOCASE_CHARACTERS+UPCASE_CHARACTERS+SYMBOLS

# print("_"*(l+24))
# for j in range(k):
# 	pa=""
# 	for i in range(l):
# 		pa=pa+random.choice(My_Combination)
	
# 	p=f"| Your password is:  {pa}  |"
# 	print(p)
# 	print("_"*len(p))




#Type2:
import random

l=int(input("Enter the lenth of password ="))
# l=15   #This value is taken for testing purpose

k=int(input("Enter the quantity of passwords ="))
# k=10  #This value is taken for testing purpose


DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']



My_Combination=DIGITS+LOCASE_CHARACTERS+UPCASE_CHARACTERS+SYMBOLS




print("_"*(l+22))    # Printing the Header line in output. Here we are muliplying "_" with lenth of "l(length of password given by user) + 22(it is length of "| Your password is: {pa} |" in line 95)" 

for j in range(k):
	pa=""  #Variable to store the password
	q=0    #Variable to store number of lowercase in password
	r=0    #Variable to store number of uppercase in password
	s=0    #Variable to store number of numbers in password
	t=0    #Variable to store number of symbols in password

	for i in range(l):
		rc=random.choice(My_Combination)  #Here we are taking a random character from Upper, Lower, Numeric and Symbols. 
		pa=pa+rc
		if rc.islower():       #Checking the lower-case charcters
			q=q+1
		elif rc.isupper():     #Checking the upper-case charcters
			r=r+1
		elif rc.isnumeric():   #Checking the numeric values
			s=s+1
		else:                  #Here we are geting the number of symbols
			t=t+1


	#Here we are printing all the output in Row-Columns(Tabular) format.  		
	p=f"| Your password is: {pa} |"
	print(p)
	print(f"| No. Of Lowercase: {q}{' '*(l)}|")  #Here we are printing the values and also adding gaps to fill up the table using " {' '*(l)} ".
	print(f"| No. Of Uppercase: {r}{' '*(l)}|")  
	print(f"| No. Of Numbers: {s}{' '*(l+2)}|")	 		
	print(f"| No. Of Symbols: {t}{' '*(l+2)}|")
	print("_"*len(p))             #Here we are printing the footer line. Actually we are printing "_" multiple to the lenth of space taken by "| Your password is: {pa} | " in line 95.     






