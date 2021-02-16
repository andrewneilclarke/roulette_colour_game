import random
import time

# assign roulette numbers to colours
red, black, green = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36], [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35], [0]

game_still_going = True
broke = False
colour_choice = ""
roll_result = ""
win_red = False
win_green = False
win_black = False
lose = False
bank = 0
betamount = 0
resulting_number = None

#welcome user
def intro():
    global bank
    print('Welcome to Roulette!! \n')
    time.sleep(0.5)
    bank = int(input('Enter starting bankroll: '))

def display_table():
    print("Roulette Table")
    print("Red: ")
    print(red)
    print("Black:")
    print(black)
    print("Green:")
    print(green)

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

def roll_ball():
    global roll_result
    global resulting_number
    #produce random spin
    resulting_number = random.randint(0, 35)
    #check which colour random number is and assign to colour as result
    if resulting_number in red:
        roll_result = "Red"
    elif resulting_number in black:
        roll_result = "Black"
    elif resulting_number in green:
        roll_result = "Green"
    print(roll_result, resulting_number)

def check_win():
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
    elif colour_choice == "b" and roll_result == "Black":
        win_black = True
        print("Black wins!")
    elif colour_choice == "g" and roll_result == "Green":
        win_green = True
        print("Green wins!!")
    else:
        lose = True
        print("You lose! €" + str(betamount))
    
def check_if_broke():
    global broke
    if bank < 1:
        broke = True
        print("Broke! Please leave!")

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
    if input("Continue? (y/n)").strip().lower() != 'y':
        break
