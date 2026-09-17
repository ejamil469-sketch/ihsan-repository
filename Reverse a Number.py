print("Q1: Reverse a Number")
num = int(input("Enter a number: "))
temp = num
negative = False
if temp < 0:
    negative = True
    temp = -temp
 
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10
 
if negative:
    rev = -rev
 
print("Reversed number:", rev)
print()