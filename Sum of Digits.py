print("Q4: Sum of Digits")
num = int(input("Enter a number: "))
temp = num
if temp < 0:
    temp = -temp
 
total = 0
while temp > 0:
    total += temp % 10
    temp = temp // 10
 
print("Sum of digits:", total)
print()