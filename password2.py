import random 
password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz@#%&*|=?/<>"
password_length=int(input("Enter the length of the password required: "))
a="".join(random.sample(password,password_length))
print(f"The password generated is: {a}")