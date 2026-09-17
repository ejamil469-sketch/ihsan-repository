print("Q5: Armstrong Number")
num = int(input("Enter a 3-digit number: "))
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp = temp // 10
 
if total == num:
    print("Armstrong")
else:
    print("Not Armstrong")
print()