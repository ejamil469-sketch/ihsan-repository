print("Q9: Largest Digit")
num = int(input("Enter a number: "))
temp = num
if temp < 0:
    temp = -temp
 
largest = 0
while temp > 0:
    digit = temp % 10
    if digit > largest:
        largest = digit
    temp = temp // 10
 
print("Largest digit:", largest)
print()