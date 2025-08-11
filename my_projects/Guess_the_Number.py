import random
x = random.randint(1, 10)
y = int(input("Enter a number between 1 to 10: "))
tries = 0

while y > x and tries < 2 :
    print("Your guess is high")
    y = int(input("Enter a number between 1 to 10: "))
    tries = tries + 1
while y < x and tries < 2 :
    print("Your guess is low")
    y = int(input("Enter a number between 1 to 10: "))
    tries = tries + 1
if y == x and tries < 2 :
    print("You have guess correct number")
elif y != x:
    print("You ran out of tries")
print(f"The correct number was {x}")
