import random
import time as t
from roulette import Roulette as r

game_still_going = True
bank = 0
betamount = 0
broke = False
colour_choice = ""
even_choice = ""
twelve_choice = ""
bet_type = None
roll = ""

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
    # take bet amount and bet type
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
            bet_type = int(input("""What would you like to bet on?\n1. Red/Black\n2. Odd/Even\n3. First twelve, second twelve, third twelve
                \nEnter a number \n"""))
        except ValueError:
            print("\nYou did not enter a valid number")
        
        if bet_type == 1 or bet_type == 2 or bet_type == 3:
            #assign colour choice
            if bet_type == 1:
                print("\nRED  -- BLACK ")
                colour_choice = (input("Red(r), black(b)? :"))
                print("€" + str(betamount) + " on " + colour_choice + "...")
            elif bet_type == 2:
                print("\nODD  -- EVEN ")
                even_choice = (input("Odd(o)or Even(e)? :"))
                print("€" + str(betamount) + " on " + even_choice + "...")
            elif bet_type == 3:
                print("\n1ST 12 -- 2ND 12 -- 3RD 12")
                twelve_choice = (input("1st 12 (1), 2nd 12 (2) or 3rd 12 (3)? :"))
                if int(twelve_choice) == 1:
                    print("€" + str(betamount) + " on 1st 12 ...")
                elif int(twelve_choice) == 2:
                    print("€" + str(betamount) + " on 2nd 12 ...")
                elif int(twelve_choice) == 3:
                    print("€" + str(betamount) + " on 3rd 12 ...")
        else:
            raise Exception


def roll_ball():
    global roll
    roll = r()
    t.sleep(2.0)

def check_win():
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
    #check colour against result 
    print("Result: " + str(roll.number) + " " + roll.colour)
    t.sleep(1)
    if bet_type == 1:  
        if colour_choice.upper() in roll.colour:
            win = True
            print(roll.colour + " wins! You win €" + str(betamount * 2))
        else:
            lose = True
            print("You lose! €" + str(betamount))
    #check odd/even against result
    elif bet_type == 2:
        if even_choice.upper() == "O" and roll.is_even() == False:
            win = True
            print("Odd wins! You win €" + str(betamount * 2))
        elif even_choice.upper() == "E" and roll.is_even() == True:
            win = True
            print("Even wins! You win €" + str(betamount * 2))
        else:
            lose = True
            print("You lose! €" + str(betamount))
    #check twelve against result
    elif bet_type == 3:
        print(roll.check_twelve() + "!")
        if twelve_choice.upper() == 1 and roll.check_twelve() == "First 12":
            win = True
            print("You win €" + str(betamount * 3))
        elif twelve_choice.upper() == 2 and roll.check_twelve() == "Second 12":
            win = True
            print("You win €" + str(betamount * 3))
        elif twelve_choice.upper() == 3 and roll.check_twelve() == "Third 12":
            win = True
            print("You win €" + str(betamount * 3))
        else:
            lose = True
            print("You lose! €" + str(betamount))

def increment_bank():
    global bank
    if win == True and bet_type == 3:    
        bank = bank+(betamount * 3)
    elif win == True:
        bank = bank+(betamount * 2)
    elif lose == True:    
        bank = bank - betamount
    t.sleep(1)
    print("Bank €" + str(bank))

def check_if_broke():
    global broke
    if bank < 1:
        broke = True
        print("Broke! Please leave!")


def play_game():
    display_table()
    take_bet()
    roll_ball()
    check_win()
    increment_bank()
    check_if_broke()

intro()
# loop main program until answer not "Y"
while game_still_going:
    play_game()
    if broke == True:
        break 
    if input("Continue? (y/n)").strip().upper() != 'Y':
        break