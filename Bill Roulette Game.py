import random

namesSTR = input("ENTER NAMES OF THE PARTICIPANTS : ")
names = namesSTR.split(",")

# print(names)

num = len(names)
index = random.randint(0, num)
person_name = names[index]
print(f"{person_name} is going to pay today")