# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import logo
import random
import replit

start_game = True


def logic(life):
    while life != 0:
        if life != 1:
            print(f"You have {life} attempts remaining to guess the number.")
        else:
            print(f"You have {life} attempts remaining to guess the number.😰")

        user_guess = int(input("Make a guess : "))
        if user_guess == guess_number:
            print("You won!! 🥳🍾")
            print(f"Guessed number was {guess_number}")

            global start_game
            choice = input("Do you want to continue Yes/No?🤔").lower()
            if choice == "no":
                start_game = False
            else:
                break
        else:
            if user_guess > guess_number:
                print("Too high.😟")
            elif user_guess < guess_number:
                print("Too low.😟")
            if life != 1:
                print("Guess again.")

            life -= 1

        if life == 0:
            print("Oh no you lost😭")
            user_continue = input("Do you want to try again Yes/No?🤔 ").lower()
            if user_continue == "no":
                start_game = False


while start_game:
    replit.clear()
    print(logo.logo)
    print("Welcome to the Number Guessing Game! ")
    guess_number = random.randint(1, 100)
    # print(f"Guessed number {guess_number}")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        life = 10
        logic(life)
    elif level == "hard":
        life = 5
        logic(life)
    else:
        print("Oops you entered an invalid input 😅 ")
        user_continue = input("Do you want to try again Yes/No?🤔 ").lower()
        if user_continue == "no":
            start_game = False
        elif user_continue != "yes":
            break