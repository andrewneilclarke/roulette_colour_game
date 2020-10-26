import random
import time

#no error handling

def main():

  print('Welcome to Roulette! \n')
  time.sleep(0.5)
  
  roulette = random.randint(-1, 35)
  #assign numbers to colours
  red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
  black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
  green = [0]
  

  #assign bet amount
  betamount = int(input("Bet amount? "))
  print("€"+str(betamount))
  #assign colour
  colour = str(input("Red(r), black(b), or green(g)? :"))
  print("€"+str(betamount)+" on "+colour)
  

  #check which colour random number is and assign to colour string 
  if roulette in red:
      rolltable="Red" #red
  elif roulette in black:
      rolltable="Black" #black
  elif roulette in green:
      rolltable="Green" #green
  #check bet (rbg) assign to rollhand string
  if colour == "r":
      rollhand="Red"
  elif colour == "b":
      rollhand="Black"
  elif colour == "g":
      rollhand="Green"
  #check rollhand against rolltable and print win/lose and amount
  if rollhand == rolltable and rollhand == "Red":
      time.sleep(0.5)
      print(rolltable, roulette, "you win €"+ str(betamount*2))
  elif rollhand == rolltable and rollhand == "Black":
      print(rolltable, roulette, "you win €"+ str(betamount*2))
  elif rollhand == rolltable and rollhand == "Green":
      print(rolltable, roulette, "you win €"+ str(betamount*35))
  else:
      print(rolltable, roulette, "You lose! €" + str(betamount)) 
#loop main program until answer not "Y" 
while True:
    main()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break
