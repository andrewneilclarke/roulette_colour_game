import random
import time
from roulette import Roulette as r

bank = 0
betamount = 0
colour_choice = ""
even_choice = ""
twelve_choice = ""
bet_type = None

#welcome user
def intro():
    global bank
    print('Welcome to Roulette! \n')
    bank = int(input('Enter starting bankroll: '))

def display_table():
    print("Roulette Table")
    print("Red: ")
    print(r.red)
    print("Black:")
    print(r.black)
    print("Green:")
    print(r.green)
    
def take_bet():
    # take bet on colour
    global colour_choice
    global even_choice
    global twelve_choice
    global betamount
    global bank
    global bet_type
    #reset variables
    betamount = 0
    colour_choice = ""
    even_choice = ""
    twelve_choice = ""
    bet_type = None
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
        
    while bet_type == None:
        #assign bet type
        try:
            bet_type = int(input("""What would you like to bet on?\n1. Red/Black\n2. Even/Odd\n3. First twelve, second twelve, third twelve
                \nEnter a number \n"""))
        except ValueError:
            print("\nYou did not enter a valid number")
        
        if bet_type == 1 or bet_type == 2 or bet_type == 3:
            #assign colour choice
            if bet_type == 1:
                print("RED  -- BLACK ")
                colour_choice = (input("Red(r), black(b)? :"))
                print("€" + str(betamount) + " on " + colour_choice)
            elif bet_type == 2:
                print("EVEN  -- ODD ")
                even_choice = (input("Odd(o)or Even(e)? :"))
                print("€" + str(betamount) + " on " + even_choice)
            elif bet_type == 3:
                print("1ST 12 -- 2ND 12 -- 3RD 12")
                twelve_choice = (input("1st 12 (1), 2nd 12 (2) or 3rd 12 (3)? :"))
                print("€" + str(betamount) + " on " + twelve_choice) 
        else:
            raise Exception


def check_win():
    #check win (FOR COLOUR!)
    global win
    global lose
    global result
    global bet_type
    global colour_choice
    global even_choice
    global twelve_choice
    #reset outcomes
    win = False
    lose = False
    print(colour_choice.upper())
    print(r1.colour)
    #check colour against result 
    print("Result: " + str(r1.number) + " " + r1.colour)  
    if bet_type == 1:  
        if colour_choice.upper() in r1.colour:
            win = True
            print(r1.colour + " wins! You win €" + str(betamount * 2))
        else:
            lose = True
    elif bet_type == 2:
        if even_choice.upper() in r1.is_even:
            win = True
            print(even_choice + " wins! You win €" + str(betamount * 2))
        else:
            lose = True
    elif bet_type == 3:
        if twelve_choice.upper() in r1.check_twelve:
            print(twelve_choice)
            print(r.check_twelve)
            win = True
    else:
        lose = True
    if lose == True:
        print("You lose! €" + str(betamount))  


def increment_bank():
    global bank
    if win == True:
        bank = bank+(betamount * 2)
    elif lose == True:
        bank = bank - betamount
    print(bank)

def check_if_broke():
    global broke
    if bank < 1:
        broke = True
        print("Broke! Please leave!")

print(r.spins)

#create instances
r1 = r()
r2 = r()
r3 = r()

print(r.spins)

#print(r.__dict__)
#print(r1.check_colour())
#print(r.check_colour(r1))
#print(colour_choice.lower())
#print(r1.colour)
#print(r1.check_twelve())
#print(r1.is_even())
#print(r.spins)

intro()
display_table()
take_bet()
check_win()
increment_bank()
check_if_broke()

"""

game_still_going = True
broke = False
win = False
lose = False






def play_game():
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