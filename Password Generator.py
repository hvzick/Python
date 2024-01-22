import random

numbers = "1234567890"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYX"
symbols = "~-_!@#&"

x = int(input("Enter how many numbers you want in your password : "))
y = int(input("Enter how many letters you want in your password : "))
z = int(input("Enter how many symbols you want in your password : "))

password = ""

for l in range(1, y+1):
    password += random.choice(letters)
for n in range(1, x+1):
    password += random.choice(numbers)
for s in range(1, z+1):
    password += random.choice(symbols)

newPass = list(password)
# print(newPass)
random.shuffle(newPass)
# print(newPass)

advPass = ""

for adv in newPass:
    advPass += adv

print(f"Your new password is {advPass}")