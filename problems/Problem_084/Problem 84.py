"""
Refactored on Thu Aug 19 2021

@author: Lucas Deutschmann
"""

from random import randint

DICE_SIZE = 4
MOVES = 10**6

GO = 0
A1 = 1
CC1 = 2
A2 = 3
T1 = 4
R1 = 5
B1 = 6
CH1 = 7
B2 = 8
B3 = 9
JAIL = 10
C1 = 11
U1 = 12
C2 = 13
C3 = 14
R2 = 15
D1 = 16
CC2 = 17
D2 = 18
D3 = 19
FP = 20
E1 = 21
CH2 = 22
E2 = 23
E3 = 24
R3 = 25
F1 = 26
F2 = 27
U2 = 28
F3 = 29
G2J = 30
G1 = 31
G2 = 32
CC3 = 33
G3 = 34
R4 = 35
CH3 = 36
H1 = 37
T2 = 38
H2 = 39

def roll():
    return [randint(1,DICE_SIZE), randint(1,DICE_SIZE)]

def CommunityChest(player, CC):
    if (CC == 0):
        return GO
    elif (CC == 1):
        return JAIL
    else:
        return player

def Chance(player, CH):
    if (CH == 0):
        return GO
    elif (CH == 1):
        return JAIL
    elif (CH == 2):
        return C1
    elif (CH == 3):
        return E3
    elif (CH == 4):
        return H2
    elif (CH == 5):
        return R1
    elif (CH == 6 or CH == 7):
        # Next Railway Company
        if (player == CH1):
            return R2
        elif (player == CH2):
            return R3
        else:
            return R1
    elif (CH == 8):
        # Next Utility Company
        if (player == CH2):
            return U2
        else:
            return U1
    elif (CH == 9):
        # Go back 3 squares
        return player-3
    else:
        return player



Field = [0] * 40
player = 0
dbl = 0
CC = randint(0, 15)
CH = randint(0, 15)

for i in range(0, MOVES):
    # Roll
    R = roll()

    # Check for double
    if R[0] == R[1]:
        dbl += 1
    else:
        dbl = 0
        
    if dbl == 3:
        dbl = 0
        player = JAIL
    else:
        player = (player+R[0]+R[1])%40

        # Community Chest
        if (player == CC1 or player == CC2 or player == CC3):
            player = CommunityChest(player, CC)
            CC = (CC+1)%16
        # Chance
        elif (player == CH1 or player == CH2 or player == CH3):
            player = Chance(player, CH)
            CH = (CH+1)%16
        # G2J
        elif player == G2J:
            player = JAIL

    Field[player] += 1

#for i in range(len(Field)):
#    print(i, 100*Field[i]/MOVES)

Maxima = sorted([(x,i) for (i,x) in enumerate(Field)], reverse=True)[:3]

print([i for (x, i) in Maxima])


















