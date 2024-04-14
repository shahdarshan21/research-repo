import random
secret_number = 4
guess = random.randint(1,5)
print(guess)
if guess == secret_number:
    print(f"congratulations! You guessed the correct number: {secret_number}")
else:
    