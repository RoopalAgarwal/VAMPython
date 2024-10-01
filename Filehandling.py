# create file for saving my laptop password
# open function will create the file when file doesn't exixts and write the file
myPassword = open("password.txt","w")

# write my laptop password in file
myPassword.write("My Laptop Password is - ghuighui\n")

#Overwrite the new password using user input
myPassword.write(input("Enter new password: "))

#read the password from file
myPassword = open("password.txt","r")

# find keyword exists or not
mydata  = myPassword.read()
if "Laptop" in mydata:
    print("Yes")
else:
    print("No")    

#to close the file
myPassword.close()

# delete the file    
import os
os.remove("password.txt")