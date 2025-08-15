
# NUMBER GUESSING GAME: USING PYTHON..................

import random

def play_game():
    
    secret_number = random.randint(1,100)
    
    print("\n======= WELCOME TO NUMBER GUESSING GAME ========")
    print("I,ve picked a number from (1-100). Can you guess?\n")
    
    attempts = 8
    
    while True:
        try:
            user_guess = int(input("Your Guess: "))
            
            if user_guess > secret_number:
                print("Too High! 🔼 Try again!")
            elif user_guess < secret_number:
                print("Too Low! 🔽 Try again!")
                attempts = attempts -1
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            if attempts == 0:
                print(f"Game over! Attempts left {attempts}! The number was {secret_number}.")
                break
        except ValueError:
            "Invalid integer! Please enter a valid number!"
            

play_game()