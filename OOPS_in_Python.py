#Object oriented programming -> object (everything is object)
#Class -> Its is a container which collects variables, functions
#example -> Tripti class 
#tripti.fullname = "triptisahu"
#tripti.age = 19
#tripti.sleeping()
#tripti.eating()
#tripti.watching()
#class syntax - class Classname:
#                            statement

class Classname:
    print("This is my class")

class Roopal:
    age = 19
    fullname = "Roopal Agarwal"
    email = "roopalk04@gmail.com"
    watching = "I love to watch BTS"
    def pocketMoney(this, amount):
        print("My pocket money is: ", amount) 

    def monthlySalary(this, daysalary):
        totalSalary = daysalary*31
        print("Your monthly salary is: ",totalSalary)    
        
#create class object
roopal:Roopal = Roopal()
print("My name is ",Roopal.fullname , "my age is ", Roopal.age,  "my email is ", Roopal.email)
roopal.pocketMoney(5000)
#roopal.pocketMoney(int(input("Enter your pocket money: ")))
print(Roopal.watching)
roopal.monthlySalary(int(input("Enter your one day salary: ")))