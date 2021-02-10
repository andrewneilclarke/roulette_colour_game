import random
import time
import roulette as r

bank = 0
roll_result = 0
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
    print(r.Roulette.get_number())
    #print(r.Roulette())
    #print(roll_result)
    #print(J.is_even())
    #print(J.check_twelve())
    #print(J.store_results(x, 5))

def handle_turn():
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
    print(r.Roulette.is_even(x, 5))
    #print(J.check_twelve())
    #print(J.store_results(x, 5))

def check_win():
    #check win (FOR COLOUR!)
    global win_black
    global win_red
    global win_green
    global lose
    #reset outcomes
    win_red = False
    win_green = False
    win_black = False
    lose = False
    #check colour against result 
    if colour_choice == "r" and roll_result == "Red":
        win_red = True
        print("Red wins!")
    """
    elif colour_choice == "b" and roll_result == "Black":
        win_black = True
        print("Black wins!")
    elif colour_choice == "g" and roll_result == "Green":
        win_green = True
        print("Green wins!!")
    else:
        lose = True
        print("You lose! €" + str(betamount))
"""

intro()
display_table()
roll_ball()
handle_turn()
#check_win()

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

"""
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