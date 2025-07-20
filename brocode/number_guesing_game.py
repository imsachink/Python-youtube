# This code is a simple number guessing game where the user has to guess a randomly generated number within a specified range.
import random 

def number_guessing_game(low, high):      

    print("----Welcome to the Number Guessing Game!----")
    print(f"I'm thinking of a number between {low} and {high}.")   
    
    guesses = 0
    guessed = False

    lucky_num = random.randint(low,high)
    

    while not guessed:
        input_num = int(input(f'enter the number between {low} and {high} : '))
        if input_num > lucky_num:
            print('input number is higher, Try Lower')
            guesses+=1
            
        elif input_num < lucky_num:
            print('input number is lower, Try Higher')
            guesses+=1
        else:
            print(f' Lucky number is {lucky_num} \n You guessed in {guesses} guesses')
            guessed =  True


low = input(' Enter lowest number : ')
high = input('Enter highest number : ')

if not (low.isdigit() or high.isdigit()):
        print('---Please enter numbers only---')
elif int(low) >= int(high):
        print('---Please enter a valid range---')
else:
    number_guessing_game(int(low), int(high))

