import random

easy_mode = 10
hard_mode = 5

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

randnumber = random.randint(1,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def check_answer(turns):
    while turns != 0:
        guessno = int(input("Make a guess:"))
        if randnumber == guessno:
            print(f"You got it. The answer was {guessno}")
            break
        elif guessno > randnumber:
            print("Too high.")
            turns = turns - 1
        elif guessno < randnumber:
            print("Too low.")
            turns = turns - 1
    if turns == 0 and guessno != randnumber:
        print("You've run out of guesses, you lose.")     

if difficulty == "easy":
    turns = easy_mode
    print(f"You have {easy_mode} attempts remaining to guess the number.")
    check_answer(turns)

elif difficulty == "hard":
    turns = hard_mode
    print(f"You have {hard_mode} attempts remaining to guess the number.")
    check_answer(turns)

        