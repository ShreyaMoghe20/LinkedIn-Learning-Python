import random
import time

def get_valid_guess():
    while True:
        try:
            guess = int(input("What is your guess? (Enter a number between 1 and 50): "))
            if 1 <= guess <= 50:
                return guess
            else:
                print("Please enter a number between 1 and 50.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

print("Hello, Welcome to the guessing game. Guess a number between 1 to 50")
time.sleep(2)

correct_number = random.randint(1, 50)
guess_count = 1
guess = get_valid_guess()  # Using the input validator function

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        print("Wrong! You need to guess Higher.")
    elif guess > correct_number:
        print("Wrong! You need to guess Lower.")
        
    guess = get_valid_guess()  # Validate input again after each wrong guess

print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")
