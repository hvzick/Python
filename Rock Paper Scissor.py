import random

user = 0
bot = 0
def rps(a):
    global user,bot
    b = random.randint(1, 3)

    if a == 2 and b == 1:
        user += 1
        print(f"You Won. You Chose Paper {a}, Computer Chose Rock {b}")

    elif a == 1 and b == 2:
        bot += 1
        print(f"Computer Won. You Chose Rock {a}, Computer Chose Paper {b}")

    elif a == 3 and b == 2:
        bot += 1
        print(f"You Won. You Chose Scissor {a}, Computer Chose Paper {b}")

    elif a == 2 and b == 3:
        user += 1
        print(f"Computer Won. You Chose Paper {a}, Computer Chose Scissor {b}")

    elif a == 3 and b == 1:
        bot += 1
        print(f"Computer Won. You Chose Scissor {a}, Computer Chose Rock {b}")

    elif a == 1 and b == 3:
        user += 1
        print(f"You Won. You Chose Rock {a}, Computer Chose Scissor {b}")

    elif a == 1 and b == 1:
        print(f"Draw. You Chose Rock {a}, Computer Chose Rock {b}")
    elif a == 2 and b == 2:
        print(f"Draw. You Chose Paper {a}, Computer Chose Paper {b}")
    elif a == 3 and b == 3:
        print(f"Draw. You Chose Scissor {a}, Computer Chose Scissor {b}")

    print(f"Your Score = {user}, Computers Score = {bot}")
    print("")

while True:

    print("Enter 0 to Exit")
    print("Enter 1 for Rock")
    print("Enter 2 for Paper")
    x = int(input("Enter 3 for Scissor "))
    if x == 0:
        print("Ended the program")
        break
    elif x > 3 or x < 0:
        print("Invalid input")
    rps(x)




