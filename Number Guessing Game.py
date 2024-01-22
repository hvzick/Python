import random

print("Enter the numbers you want to guess between")
z = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))


def guess(a, b):
    r = random.randint(a, b)
    c = 0
    while True:
        x = int(input(f"Guess the number from {a} - {b} : "))
        if x < a or x > b:
            print("Guessed number is out of bounds")
        elif x > r:
            print("Guessed number is higher than actual number")
            c = c + 1
        elif x < r:
            print("Guessed number is lower than actual number")
            c = c + 1
        elif x == r:
            c = c + 1
            print(f"You have guessed the number {r} correctly in {c} tries")
            break


guess(z, y)
