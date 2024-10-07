#create first python project to generate 6 digit random otp

import random

def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

print("Your 6-digit OTP is:", generate_otp())

#WAP to convert dollar into rupees and vice versa

def convert_currency():
    # Exchange rate (1 USD = 74.83 INR, you can update this value as per current exchange rate)
    exchange_rate = 74.83

    print("1. Convert Dollars to Rupees")
    print("2. Convert Rupees to Dollars")
    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        dollars = float(input("Enter amount in Dollars: "))
        rupees = dollars * exchange_rate
        print(f"{dollars} USD is equal to {rupees} INR")
    elif choice == 2:
        rupees = float(input("Enter amount in Rupees: "))
        dollars = rupees / exchange_rate
        print(f"{rupees} INR is equal to {dollars} USD")
    else:
        print("Invalid choice")

convert_currency()


#WAP to find the age in years, month and days when the birth year is given
#for current time
cyear=int(input("the current year: "))
cmonth=int(input("the current month: "))
cday=int(input("the current day: "))
print("year :",cyear,"\nmonth : ",cmonth,"\nday : ",cday)

#for birth time
byear=int(input("the birth year: "))
bmonth=int(input("the birth month: "))
bday=int(input("the birth day: "))
print("year :",byear,"\nmonth : ",bmonth,"\nday : ",bday)

#main logic
year=cyear-byear
month=cmonth-bmonth
day=cday-bday

if day<0 :
    month-=1
    day+=30
if month<0 :
    year-=1
    month+=12

print("year : ", year,"month : ", month,"day : ", day)