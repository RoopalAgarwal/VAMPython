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

#Error 6
dict = {1: "Roopal", 2: "Raj"}
#dict[4]        
try:
    dict[4]
except KeyError:                     #when  key is not present in dictionary

    print("Error 6 - The key doesn't exist in the dictionary")


#Error 7
# a=10
# b=20
# c=a+b
#  #   print(c)
# try: 
#     print(c)
# except IndentationError:
#     print("Error 7 - unindent does not match any outer indentation level")   #means gap is the problem

#Error 8
#no = int(input("Enter no. = "))
#print(no)
try:
    no = int(input("Enter no. = "))
except ValueError:
    print("Error 8 - invalid type of data entered ")

#Error 9
#except BufferError: