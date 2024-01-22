import random

rollAgain = "y"

while rollAgain == "y":
     r1 = random.randint(1, 6)
     r2 = random.randint(1, 6)

     print(f"Dice 1 {r1}")
     print(f"Dice 2 {r2}")
     rollAgain = input("y to roll again, n to stop")

