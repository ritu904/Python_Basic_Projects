import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS =5
def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else :
        return HARD_LEVEL_ATTEMPTS
    
def check_number(guessed_number,random_number, attempts):
    if guessed_number<random_number:
        print("Your guess is too low")
        return attempts-1
    elif guessed_number>random_number:
        print("Your guess is too high")
        return attempts-1
    else :
        print(f"Your answer is right....The answer was {random_number}")
def game():
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")

    random_number = random.randint(1,50)
    print(random_number)

    level = input("choose difficulty level.....Type 'easy' or 'hard':")
    attempts= set_difficulty(level)

    #print(f"You have {attempts} remaining to guess the number.")
    guessed_number=0
    while guessed_number!=random_number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number=int(input("guess a number:"))
        attempts=check_number(guessed_number,random_number, attempts)

        if attempts==0:
         print("No attempts left")
         return
        elif guessed_number!=random_number:
          print("Guess again")

game()