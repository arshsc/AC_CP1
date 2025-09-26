# AC 2nd Fix Game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        # Guess input needs to be an int / Run-time / a string cannot equal an int
        guess = int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        # This if needs to be an elif / Logic / It is one conditional all throughout
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        # There is an unlimited amount of attempts / Logic / The game never ended
            attempts += 1
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            attempts += 1
        # Needs an else statement / Logic / Just in case a condition isn't met
        else:
            print("This shouldn't be possible")
        # Continue statement did not need to be there / Logic / Not useful
    print("Game Over. Thanks for playing!")
start_game()