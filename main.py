import random

print("Welcome to our $HIT Penalty SHootout Game!")

Pscore = 0
Escore = 0

gp= """
----------------------------------------
I                                      I
I 0               1                  2 I
I                                      I
I 3               4                  5 I
I                                      I
I 6               7                  8 I
I                                      I
---------------------------------------- 
"""

s = int(input("How many shots will each team get? "))

for i in range(s):
    print("Take the "+str(i+1)+" shot")
    print(gp)
    shot = int(input("Choose where you want to shoot (1-8): "))
    if shot < 1 or shot > 8:
        print("Invalid Chosen")
        shot = int(input("Choose where you want to shoot (1-8): "))
    else:
        pass
    print("You shooted at the "+str(shot)+" point")
    AIkeep = random.randint(1,8)
    print("AI dived "+str(AIkeep))

    if (shot == AIkeep):
        print("SHOT SAVED!!")
    else:
        print("YOU SCORED!")
        Pscore += 1
    
    print("Try to save the shot")
    Eshot=random.randint(1,8)
    keep = int(input("Where you want to dive? (1-8)"))

    print("Enemy shooted at "+str(Eshot))

    if (Eshot == keep):
        print("YOU SAVED!!")
    else:
        print("THEY SCORED!!")
        Escore+=1

    print("ENEMY SCORE: "+str(Escore))
    print("PLAYER SCORE: "+str(Pscore))

if Pscore>Escore:
    print("YOU WON!!")
elif Escore>Pscore:
    print("YOU LOST!!")
else:
    print("YOU DREW!!")