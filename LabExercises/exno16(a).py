import random
player1=0
player2=0
p1=0
p2=0
while(1):
    print("Do you want to roll the dice (Y/N)")
    ch=input()
    if ch=='N':
        break
    else:
        print("Player 1 is rolling the dice: ",end=" ")
    p1=random.randint(1,6)
    player1+=p1
    print(p1)
print("Player 2 is rolling the dice: ",end=" ")
p2=random.randint(1,6)
player2+=p2
print(p2)
print()
print()
if player1>player2:
    print("Player 1 has won!!!")
elif player2>player1:
    print("Player 2 has won!!!")
else:
    print("The game ended in a tie!!!")