import random

def spin():
    symbols = ("⭐","♥️","♦️","🔔", "🍉")
    return [random.choice(symbols) for _ in range(3)]

def show(row):
    print("  ".join(row))

def pay(bet,row):
    if row[0] == row [1] == row[2]:
        if row[0] == "⭐":
            return bet*2
        elif row[0] == "♥️":
            return bet*5
        elif row[0] == "♦️":
            return bet*7
        elif row[0] == "🔔":
            return bet*10
        else :
            return bet*15
    else : return 0





def main():
    balance = 100
    print("*****************************")
    print('****Welcome to the Casino****')
    print("*****************************")

    print('Symbols are ⭐ ♥️  ♦️  🔔 🍉')
    print("*****************************")

    flag = True
    while flag:
        print(f'Your Current Balance is {balance}')
        bet = input('Place your bet  : ')  
        if not bet.isdigit():
             print('Please enter valid number')
             continue
        bet =  int(bet)
        if bet <= 0:
            print('Bet should be greater than zero')
        elif bet>balance:
            print('Your balance is low😞😞😞😞😞')
        else: 
            print(f"Your betting amount is {bet}")
            
        balance-=bet
        row = spin()
        print('Spinning.......................')
        show(row)

        payment = pay(bet,row)

        if payment > 0:
            print(f'You won {payment}')
            balance+=payment

        check = input('Please enter to continue : ')

        

        if not check == '':
            break


        if balance<=0:
            print('Your Current Balance is Low')
            break
    
    print(f'Your Current Balance is {balance}')
    print('***********Good Bye**************')
          
if __name__=='__main__':
    main()