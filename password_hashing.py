from hashlib import *

Dictionary = {
    }


    
username = input("username? ")
password = input("password? ")
#print((sha256(password.encode('utf-8')).hexdigest()))
Dictionary.update({password : ((sha256(password.encode('utf-8')).hexdigest()))})
#print(Dictionary)
print("please enter password to log in ")
Z = False
while not Z:
    x = input("password? ")
    if sha256(x.encode('utf-8')).hexdigest() == Dictionary[password]:
        print(username + ", you are logged in")
        Z = True
    else:
        print("Incorrect password")
        print("please try again")
