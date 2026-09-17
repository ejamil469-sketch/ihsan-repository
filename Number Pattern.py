print("Q12: Number Pattern")
n = int(input("Enter N: "))
 
print("Pattern A:")
i = 1
while i <= n:
    line = ""
    j = 1
    while j <= i:
        line = line + str(j)
        j += 1
    print(line)
    i += 1
 
print("Pattern B:")
i = 1
while i <= n:
    line = ""
    j = 1
    while j <= i:
        line = line + str(i)
        j += 1
    print(line)
    i += 1
print()