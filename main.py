import random
import time
from roulette import Roulette as r

bank = 0
betamount = 0
colour_choice = ""
even_choice = ""

#welcome user
def intro():
    global bank
    print('Welcome to Roulette! \n')
    time.sleep(0.8)
    bank = int(input('Enter starting bankroll: '))

def display_table():
    print("Roulette Table")
    print("Red: ")
    print(r1.red)
    print("Black:")
    print(r1.black)
    print("Green:")
    print(r1.green)
    
def take_bet():
    # take bet on colour
    global colour_choice
    global even_choice
    global betamount
    global bank
    #reset variables
    betamount = 0
    colour_choice = ""
    even_choice = ""
    while betamount == 0:
        #assign bet amount
        try:
            betamount = int(input(f"\nBet amount? (€" + str(bank) + " available)\n"))
        except ValueError:
                print('\nYou did not enter a valid amount')
    #prevent debt
    if betamount > bank:
        betamount = bank
    
    print("€" + str(betamount))
    
    bet_type = None
    while bet_type == None:
        try:
            bet_type = (input("""What would you like to bet on?\n1. Red/Black\n2. Even/Odd\n3. First twelve, second twelve, third twelve
                \nEnter a number """))
        except ValueError:
            print("\nYou did not enter a valid number")
        else:
            if bet_type != '1':
                raise Exception("\nYou did not enter a valid number!".format())
            else:
                #assign colour choice
                if bet_type == 1:
                    colour_choice = (input("Red(r), black(b), or green(g)? :"))
                    print("€" + str(betamount) + " on " + colour_choice)
                elif bet_type == 2:
                    even_choice = (input("Odd(o)or Even(e)? :"))
                    print("€" + str(betamount) + " on " + even_choice)
                elif bet_type == 3:
                    twelve_choice = (input("1st 12 (1), 2nd 12 (2) or 3rd 12 (3)? :"))
                    print("€" + str(betamount) + " on " + twelve_choice)

def odd_even_bet():
    # take bet on colour
    global colour_choice
    global betamount
    global bank
    #reset betamount
    betamount = 0
    while betamount == 0:
        #assign bet amount
        try:
            betamount = int(input(f"\nBet amount? (€" + str(bank) + " available)\n"))
        except ValueError:
                print('\nYou did not enter a valid amount')
    #prevent debt
    if betamount > bank:
        betamount = bank
    print("€" + str(betamount))
    #assign colour choice
    colour_choice = (input("Red(r), black(b), or green(g)? :"))
    print("€" + str(betamount) + " on " + colour_choice)

def twelve_bet():
    # take bet on which twelve
    global colour_choice
    global betamount
    global bank
    #reset betamount
    betamount = 0
    while betamount == 0:
        #assign bet amount
        try:
            betamount = int(input(f"\nBet amount? (€" + str(bank) + " available)\n"))
        except ValueError:
                print('\nYou did not enter a valid amount')
    #prevent debt
    if betamount > bank:
        betamount = bank
    print("€" + str(betamount))
    #assign colour choice
    colour_choice = (input("Red(r), black(b), or green(g)? :"))
    print("€" + str(betamount) + " on " + colour_choice)

def check_win():
    #check win (FOR COLOUR!)
    global lose
    global result
    #reset outcomes
    win_red = False
    win_green = False
    win_black = False
    lose = False
    #check colour against result 
    print(colour_choice.lower())
    print(r1.colour.lower())
    print(str(r1.number) + r1.colour)
    if colour_choice.lower() in r1.colour.lower():
        win_red = True
        print(r1.colour + " wins!")
    else:
        lose = True
        print("You lose! €" + str(betamount))
    


#create instances
r1 = r()
r2 = r()
r3 = r()

intro()
display_table()
take_bet()
#print(spin1.get_colour())
#handle_turn()
check_win()



"""
print(r1.number)
print(r1.colour)
print(r1.is_even())
print(r1.check_twelve())

print(r2.number)
print(r2.colour)
print(r2.check_twelve())

game_still_going = True
broke = False
win_red = False
win_green = False
win_black = False
lose = False


    
def check_if_broke():
    global broke
    if bank < 1:
        broke = True
        print("Broke! Please leave!")
    else:
        pass

def increment_bank():
    global bank
    if win_red == True:
        bank = bank+(betamount * 2)
    elif win_black == True:
        bank = bank+(betamount * 2)
    elif win_green == True:
        bank = bank+(betamount * 35)
    elif lose == True:
        bank = bank - betamount
    print(bank)


def play_game():
    handle_turn()
    roll_ball()
    check_win()
    increment_bank()
    check_if_broke()

intro()
display_table()
# loop main program until answer not "Y"
while game_still_going:
    play_game()
    if broke == True:
        break
    if input("Continue? (y/n)").strip().upper() != 'Y':
        break
"""