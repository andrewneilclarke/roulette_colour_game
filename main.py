import random
import time
from roulette import Roulette as r

bank = 0
result = 0
betamount = 0
colour_choice = ""

#welcome user
def intro():
    global bank
    print('Welcome to Roulette! \n')
    time.sleep(0.5)
    bank = int(input('Enter starting bankroll: '))

def display_table():
    print("Roulette Table")
    print("Red: ")
    print(r.red)
    print("Black:")
    print(r.black)
    print("Green:")
    print(r.green)

def roll_ball():
    global result
    result = (r().spin_wheel())
    print(result)
    return result
    
def take_bets():
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
    time.sleep(0.5)
"""

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
    if result in r.red:
        #win_red = True
        print("Red wins!")
    elif result in r.black:
        #win_black = True
        print("Black wins!")
    elif result in r.green:
        #win_green = True
        print("Green wins!!")
    
    #else:
    #    lose = True
    #    print("You lose! €" + str(betamount))


#store a number of spins in a list
results = []
for i in range(12):
    print(r().spin_wheel())
    print(check_win())
"""
#intro()
#display_table()
#take_bets()
#roll_ball()
#print(spin1.get_colour())
#handle_turn()
#check_win()

#create instances
r1 = r()
r2 = r()
r3 = r()

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
"""

    
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