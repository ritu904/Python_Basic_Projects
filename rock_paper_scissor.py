import random
user_choice = int(input("Type 0 for rock. 1 for paper, 2 for scissor:"))
if user_choice>=3 or user_choice<0:
    print("you entered invalid number. You lose")
else:
    computer_choice = random.randint(0,2)
    print(computer_choice)

    if computer_choice==user_choice:
        print("it's a draw.")
    elif computer_choice == 0 and user_choice==2:
        print("You lose")
    elif computer_choice == 2 and user_choice==0:
        print("You win")
    elif computer_choice>user_choice:
        print("you lose")
    elif computer_choice<user_choice:
        print("you win")
