import random
values = ["rock" , "paper" , "scissor"]

user_picks = input(" What do you choose ? Rock Paper or Scissor\n")
computer_picks = random.choice(values)

if(user_picks == computer_picks):
    print("It's a tie !")
else:
    if(user_picks == "rock" and computer_picks == "paper"):
        print("Computer picks paper ! You Looose  ! Cry! Cry! Cry!")
    elif(user_picks == "rock" and computer_picks == "scissor"):
        print("Computer picks Scissor ! You won ! Ha! Ha! Ha!")
    elif(user_picks == "paper" and computer_picks == "rock"):
        print("Computer picks rock ! You Won  ! Ha! Ha! Ha!")
    elif(user_picks == "paper" and computer_picks == "scissor"):
        print("Computer picks Scissor ! You Looose  ! Cry! Cry! Cry!")
    elif(user_picks == "scissor" and computer_picks == "rock"):
        print("Computer picks rock ! You Looose  ! Cry! Cry! Cry!")
    elif(user_picks == "scissor" and computer_picks == "paper"):
        print("Computer picks paper ! You won ! Ha! Ha! Ha!")

    

