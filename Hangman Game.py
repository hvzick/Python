life1 = "+-----+\n|     |\n|\n|\n|\n|______ \n"
life2 = "+-----+\n|     |\n|\n|\n|\n|\n"
life3 = "+-----+\n|     |\n|     0\n|\n|\n|\n"
life4 = "+-----+\n|     |\n|     0\n|    /|\\ \n|\n|\n"
life5 = "+-----+\n|     |\n|     0\n|    /|\\ \n|    / \\ \n|\n"
life6 = "+-----+\n|     |\n|     0\n|    /|\\ \n|    / \\ \n|_______ \n"
lives = 5
if lives == 5:
    print(life1)

p1_input = input("Enter a word for other person to guess: ").upper()
blanks = []
for i in range(0, len(p1_input)):
    blanks.append('_')
print(blanks)


guessedLetter = []
endGame = False
while not endGame:
    if lives == 4:
        print(life2)
    elif lives == 3:
        print(life3)
    elif lives == 2:
        print(life4)
    elif lives == 1:
        print(life5)

    guess = input("Enter a letter to guess the word: ").upper()

    if guess in guessedLetter:
        print("You have guessed this letter")
    else:
        guessedLetter.append(guess)

    if guess in p1_input:
        print(f"{guess} is present in the word")
    elif guess not in p1_input:
        print(f"{guess} is not present in the word")
    for position in range(0, len(p1_input)):
        letter = p1_input[position]
        if guess == letter:
            blanks[position] = letter
    if guess not in p1_input:
        lives = lives - 1

    print("Lives = ", lives)
    if lives == 0:
        endGame = True
        print(life6)
        print("You Lose")

    print(" ".join(blanks))
    if "_" not in blanks:
        endGame = True
        print("You win")
    