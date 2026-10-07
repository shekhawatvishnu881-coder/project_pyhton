import random

def play():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Guess the number between 1 and 100!")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"🎉 Correct! You got it in {attempts} attempts.")
            return

        print(f"Attempts left: {max_attempts - attempts}\n")

    print(f"Game over! The number was {secret}.")

while True:
    play()
    again = input("\nPlay again? (yes /no ): ").lower()
    if again != " yes ":
        print("Thanks for playing!")
        break
