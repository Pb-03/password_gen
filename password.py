import string
import random
length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
		1. Letters
		2. Digits
		3. Special characters
		4. Exit''')

characterList = ""
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		
		# Adding letters to possible characters
		characterList += string.ascii_letters
	elif(choice == 2):
		
		# Adding digits to possible characters
		characterList += string.digits
	elif(choice == 3):
		
		# Adding special characters to possible
		# characters
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(length):

	# Picking a random character from our character list
	randomchar = random.choice(characterList)
	password.append(randomchar)

print("The random password is " + "".join(password))
