import random

print("1.Rock")
print("2.Paper")
print("3.Scissor")

def game(a,b):

    if act1 == act2:
        print("Tie")

    if act1 == 1:
        if act2 ==2:
            print("2 win")
        elif act2 == 3:
            print("1 win")

    elif act1 ==2:
        if act2 == 1:
            print("1 win")
        elif act2 == 3:
            print("2 win")

    elif act1 == 3 :
        if act2 == 1:
            print("2 win")
        elif act2 == 2:
            print("1 win")


    else:
        print("Invalid choice")

n = int(input("Enter number of players:"))
limit = int(input("limit:"))
sc1 =0
sc2 =0

while sc1 != limit or sc2 != limit:
    if n == 1:
        act1 = int(input("enter choice of player:"))
        act2 = random.randint(1,3)
        print("computer choice is:",act2)
        score = game(act1,act2)
        if score == "1 win":
            sc1 +=1
        elif score == "2 win":
            sc2 += 1
        elif score == "Tie" :
            sc1 += 0
            sc2 += 0
        print("sc1 =",sc1)
        print("sc2=",sc2)

    elif n == 2:
        act1 = int(input("enter choice of player1:"))
        act2 = int(input("enter choice of player2:"))
        score = game(act1,act2)
        if score == "1 win":
            sc1 +=1
        elif score == "2 win":
            sc2 += 1
        elif score == "Tie" :
            sc1 += 0
            sc2 += 0
        print("sc1 =", sc1)
        print("sc2=", sc2)

    else:
        print("Invalid choice")
if sc1 == limit:
    print("player1 won")
else:
    print("player2 won")