import random

options = ["rock","paper","scissors"]


    
flag =  True

while flag:
    player =  input("Enter Your Choice (rock,paper,scissors): ").lower()
    computer =  random.choice(options)

    print(f"Player Choice : {player}")
    print(f"Computer Choice : {computer}")

    while player not in options :
        player =  input("Enter Your Choice (rock,paper,scissors): ")
    if player == computer:
            print("Tie")
    elif player == "rock" and computer == "paper":
            print("You Lose")
    elif player == "paper" and computer == "scissors":
            print("You Lose")   
    elif player == "scissors" and computer == "rock":
            print("You Lose")
    else: print("You Win")

    if input("want to play again (y/n) : ")=='y': 
            flag=True 
        
