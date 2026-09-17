print("Q10: Second Largest Digit")
num = int(input("Enter a number: "))
temp = num
if temp < 0:
    temp = -temp
 
largest = -1
second = -1
while temp > 0:
    digit = temp % 10
    if digit > largest:
        second = largest
        largest = digit
    elif digit < largest and digit > second:
        second = digit
    temp = temp // 10
 
print("Second largest digit:", second)
print()