from words import word


hangman_stages = [
    """
       _______
      |/      |
      |
      |
      |
      |
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |
      |
      |
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |       |
      |       |
      |
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|
      |       |
      |
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|/
      |       |
      |
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|/
      |       |
      |      /
     _|___
    """,
    """
       _______
      |/      |
      |      (_)
      |      \\|/
      |       |
      |      / \\
     _|___
    """
]

def show_hint(hint):
    print('*************************')
    print(" ".join(hint))
    print('*************************')

def show_ans(word):
    print('*************************')
    print(" ".join(word))
    print('*************************')

def display_hang(wrong_guesses):
    print('*************************')
    print(hangman_stages[wrong_guesses])
    print('*************************')




def main():
    hint =  ['_'] * len(word)

    wrong_guesses =0
    guessed_word = set()
    running = True
    
    while running:
        
        display_hang(wrong_guesses)       
        
        show_hint(hint) 
        
        guess = input('Please enter word : ').lower()

        if len(guess)!=1 or not guess.isalpha():
            print('invalid input')
            continue

        if guess in guessed_word:
            print(f'{guess} is already guessed')
            continue

        guessed_word.add(guess)

           
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i]=guess 
        
        else:
            wrong_guesses+=1
                      
            display_hang(wrong_guesses)
        
        if wrong_guesses>=len(hangman_stages)-1:
            display_hang(wrong_guesses)
            print('*************************')
            print('*************************')
            print('       YOU LOOSE         ')
            print('*************************')
            print('*************************')
            running = False

        elif '_' not in hint:
            print('*************************')
            show_ans(word)
            print('*************************')
            print('*************************')
            print('         YOU Win         ')
            print('*************************')
            print('*************************')
            running = False



        

    


if __name__== '__main__':
    main()
