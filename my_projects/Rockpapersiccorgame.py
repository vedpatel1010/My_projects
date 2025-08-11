import random
p = 0
c = 0
for a in range(3):
    x = random.randint(1, 3)
    y = int(input("Enter what have you chosen:\n 1) Rock \n 2) Paper \n 3) scissor \n : "))
    while y > 3:
        print("invalid option chossen")
        y = int(input("Enter what have you chosen:\n 1) Rock \n 2) Paper \n 3) scissor \n : "))

    if x == y :
        print("Both chosen same")
    elif x == 2 and y == 3:
        print("Player Wins")
        p = p + 1
    elif x ==2 and y == 1:
        print("Computer Wins")
        c  = c + 1
    elif x == 1 and y == 3:
        print("Computer Wins")
        c = c + 1
    elif x == 1 and y == 2:
        print("Player Wins")
        p = p + 1
    elif x == 3 and y == 1:
        print("Player Wins")
        p = p + 1
    elif x == 3 and y == 2:
        print("Computer Wins")
        c = c + 1
    print(f"The computer choose {x}")
print(f"The total score is Computer:{c} and Player:{p}")
if c > p:
    print("The Computer Wins!")
elif c == p:
    print("The scores were same it's a Tie!")
else :
    print("The Player Wins!")