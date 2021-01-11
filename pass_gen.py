import random 

def getPassword() :
    ''' function to generate passwords '''
    passw=""
    y=0
    while y < passw_length :
        r=random.choice(passw_set)
        passw += r
        y += 1
    return passw
yes_list=["yes","y","o"]
no_list=["no","n"]
passw_upper="QWERTYUIOPASDFGHJKLZXCVBNM"
passw_lower="qwertyuiopasdfghjklzxcvbnm"
passw_digit="0123456789"
passw_set=""
passw_length=int(input("Enter length of Your password====> "))
passw_total=int(input("Enter numbers of passwords to generate====> "))
if input("Do you want Upper characters in your password(Y / N) : ").lower() in yes_list :
    passw_set += passw_upper
if input("Do you want Lower characters in your password(Y / N) : ").lower() in yes_list :
    passw_set += passw_lower
if input("Do you want Digits(numbers) in your password(Y / N) : ").lower() in yes_list :
    passw_set += passw_digit
if len(passw_set) == 0 :
    passw_set=passw_upper+passw_lower+passw_digit
x = 0
while x < passw_total :
    x += 1
    print(getPassword())
