import random

def guess_number():
    print("10 chances to guess a number between 1 and 100")
    magic_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your answer (1-100):"))
            if guess < 1 or guess > 100:
                print("Invalid answer!")
                continue
            attempts += 1
            if guess == magic_number:
                print(f"🎉Bingo! You guessed the number in {attempts} attempts.")
                return
            elif guess < magic_number:
                print("Too low, try again.")
            else:
                print("Too high, try again.")
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"{remaining} chances remaining.")
            else:
                print(f"Game over! The answer was {magic_number}.")
        except ValueError:
            print("That's not a number.")

guess_number()