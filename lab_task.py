import math
import random

# x = int(input("ENTER A NUMBER : "))
# u = int(input("ENTER ITS POWER : "))
#
# i = x ** u
#
# # i = math.pow(x,u)
# print(f"THE POWER OF {x} is {i}")
# #

# xx = int(input("ENTER FIRST NUMBER : "))
# yy = int(input("ENTER SECOND NUMBER : "))
#
# ii = math.gcd(xx,yy)
# print(f"GCD OF {xx} and {yy} is {ii}")


# x = int(input("ENTER THE NTH NUMBER : "))
# e = 0
#
# for n in range(2, x):
#     for jj in range(2, n):
#         if n % jj == 0:
#             break
#     else:
#         print(n)

numbers = "1234567890"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYX"

x = 5
y = 3
no = ""

for rl in range(0, x+1):
    no += random.choice(letters)
for rn in range(0, y+1):
    no += random.choice(numbers)

print(no)
