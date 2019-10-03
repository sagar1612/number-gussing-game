import random
winning_number = random.randint(1,100) 
guess =1
game_over = False
name=input("enter your name : ")
while  True:
    number =int(input("guess a number between 1 and 100 :"))
    if number == winning_number:
        print(f"congratulation  {name} and you win  this game by guess  the right number in {guess} attempts")
        break
    else:
        if number < winning_number:
          print("too low")
        else:
          print("too high") 
    guess +=1
    continue
