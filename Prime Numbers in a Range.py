print("Q7: Prime Numbers in a Range")
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
 
num = start
while num <= end:
    if num > 1:
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(num, end=" ")
    num += 1
print()
print()