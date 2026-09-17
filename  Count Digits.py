print("Q3: Count Digits")
num = int(input("Enter a number: "))
temp = num
if temp < 0:
    temp = -temp
 
if temp == 0:
    count = 1
else:
    count = 0
    while temp > 0:
        count += 1
        temp = temp // 10
 
print("Number of digits:", count)
print()