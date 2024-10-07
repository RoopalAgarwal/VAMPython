#Error 1
#print(x)

#Error Handling
try:
    print(x)
except NameError:
    print("Error 1 - Variable x is not defined")

#Error 2
# y = 1/0

try:
    y = 1/0
except ZeroDivisionError:
    print("Error 2 - Division by zero")

#Error 3
name = "Roopal"
#no = int(name)    

try:
    no = int(name)
except ValueError:
    print("Error 3 - Invalid literal for int() with base 10: 'Roopal'")    

#Error 4
friends = ["Raj", "Kashish", "Tripti"] 
#friends[4]

try:
    friends[4]
except IndexError:
    print("Error 4 - List index is out of range")    

#Error 5
amount = 500
email = "roopalk04@gmail.com"
#total = amount + email
try:
    total = amount + email
except TypeError:
    print("Error 5 - String and integer cannot be concatenated")