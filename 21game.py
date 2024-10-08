import time

print("rules for the 21 game:")
time.sleep(0.5)
print("player one will start with the number 0 and can eaither add +1 or +2")
time.sleep(0.5)
print("player 2 will then also add +1 or +2")
time.sleep(0.5)
print("the game will continue until someone says 21. The winner is the person who says 21")

total = 0

while total < 21:
    player1 = int(input("player 1, pick a number between 1 and 2 "))
    total = total + player1
    print("the total is", total)
    
