print("Q15: Number Guessing Game")
secret = 37
max_attempts = 5
attempt = 1
found = False
 
while attempt <= max_attempts:
    guess = int(input("Enter your guess (attempt " + str(attempt) + "): "))
    if guess == secret:
        print("Correct!")
        found = True
        break
    elif guess > secret:
        print("Too High")
    else:
        print("Too Low")
    attempt += 1
 
if not found:
    print("Game Over. The number was", secret)
 