print("Q14: Perfect Number")
num = int(input("Enter a number: "))
total = 0
i = 1
while i < num:
    if num % i == 0:
        total += i
    i += 1
 
if total == num and num > 0:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
print()