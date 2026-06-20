import random

secret = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess (1-100): "))
    tries = tries + 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        # they got it! print a win message with `tries`, then stop the loop
        print(f"Congratulations! You guessed the number in {tries} tries.")
        break