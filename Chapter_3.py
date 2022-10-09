# Exercise 1: 

hours=int(input("Enter hours: "))
rate = float(input("Enter rate: "))
if hours > 40: 
    pay=(40*rate)+(hours-40)*rate*1.5 #without math transformations
    #pay=(1.5*hours-20)*rate
else: pay=hours*rate
print("Pay is: ", pay)

# Exercise 2: 

try:
    hours=int(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    if hours > 40: 
        pay=(40*rate)+(hours-40)*rate*1.5 #without math transformations
        #pay=(1.5*hours-20)*rate
    else: pay=hours*rate
    print("Pay is: ", pay)
except:
    print("Please enter a number")

# Exercise 3: 

try:
    score=float(input("Enter score: "))
    if 0.9 <= score <=1.0: 
            print(score, " is A")
    elif 0.8 <= score < 0.9:
            print(score, " is B")
    elif 0.7 <= score < 0.8:
            print(score, " is C")
    elif 0.6 <= score < 0.7:
            print(score, " is D")
    elif 0 <= score < 0.6:
            print(score, " is F")
    else:
        print(score, "Bad score, number is bigger than 1")
except: 
    print("Bad score, number can't be text")

#ex3 with random

# import random
# a=random.randint(0,2)
# if a==0:
#     score="good"
#     print("Bad, number can't be text")
    
# elif a==1 or a ==2:
#     score=(random.randint(0,150))/100
#     if 0.9 <= score <=1.0: 
#             print(score, " is A")
#     elif 0.8 <= score < 0.9:
#             print(score, " is B")
#     elif 0.7 <= score < 0.8:
#             print(score, " is C")
#     elif 0.6 <= score < 0.7:
#             print(score, " is D")
#     elif 0 <= score < 0.6:
#             print(score, " is F")
#     else:
#             print(score, " Number larger than 1")








