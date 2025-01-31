import random

def number_guessing_game():
    print("Welcome to the Number Guessing Adventure!")
    print("You find yourself in a mysterious land where numbers hold magical powers.")
    print("A wise old sage challenges you to guess the sacred number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your magical number: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("The number is too low! Seek higher wisdom.")
            elif guess > number_to_guess:
                print("The number is too high! Tread carefully.")
            else:
                print(f"Amazing! You have uncovered the sacred number in {attempts} attempts.")
                print("The sage nods in approval and grants you a mystical artifact.")
                break
        except ValueError:
            print("The universe only understands numbers. Try again.")

def play_again():
    while True:
        replay = input("Would you like to play again? (yes/no): ").strip().lower()
        if replay in ['yes', 'y']:
            number_guessing_game()
        elif replay in ['no', 'n']:
            print("Farewell, brave traveler!")
            break
        else:
            print("I do not understand your response. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    number_guessing_game()
    play_again()
