print("Hello World!")

#strings in python
print("""Hello 
World!""")

#integers in python
print(15)

#errors in printing data
print(1,000) #wrong way to print 1000

print(1_000) #right way to print 1000

#floats in python
print(3.14)

#boolean in python
#True
#False

#how to check certain datatype
print(type(12))

#variables in python
myName = "hazik"
print(myName)

n = 15
print(n)

#opeeatrors in python
#Arithmetic operators +-*/
#using / will give float value and using floor division// will give integer value

print(4/2)
print(4//2)

#using ** will give raise power value
print(4*2)
print(4**2)

#priority in python
#Parenthesis
#Exponents
#Multiplication
#Division
#Addition
#Subtraction

#modulus in python used to get remainder
print("Remainder is 11/3 is ")
print(11%3)

#concatenation of strings
print("hello " + "world")

#multiplying strings
print(5*"hazik ")

#taking user input
#input("what is your name ")
#print("hello " + input("whats your name"))

#newline \n
print("hello\nworld")

#length of string
#name = input("enter string to find its length")
#print(len(name))

#concatenating int and string
#name = input("enter string to find its length")
#length = len(name)
#newLength = str(length)
#print("your name has " + newLength + " characters")

# x = input("enter 1st no")
# y = input("enter 2nd no")
# z = int(x) + int(y)
# newX = str(x)
# newY = str(y)
# newZ = str(z)
# print("the sum of " + newX + " and " + newY + " is " + newZ )

# F STRINGS type f infront of a string
weeks = 52
year = 1
print(f"there are {weeks} weeks in {year} year")

#rounded off number
r = round(10/3)
print(f"rounded off number in 10/3 is {r}")

# name = input("whats your name")
# print("hello " + name)

# n = input("enter your fav color")
# y = input("enter your fav animal")
# print("your grp name is " +n+y)

#conditional if else statements
x = 55
y = 100
print(f"x = {x}")
print(f"y = {y}")
if x>y:
    print("x > y")
elif x==y:
    print("x = y")
else:
    print("x < y")
if x%2==0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")
if y % 2 == 0:
    print(f"{y} is even")
else:
    print(f"{y} is odd")

#nested conditions
xx = 77
yy = 66
print(xx)
print(yy)
if xx%2==0:
    if xx > yy:
        print(f"{xx} is even and is > {yy}")
    else:
        print(f"{xx} is even and is < {yy}")
else:
    if xx > yy:
        print(f"{xx} is odd and is > {yy}")
    else:
        print(f"{xx} is even and is < {yy}")

#chained conditional
#elif condition aka else if

#bmi calculator
weight = input("Enter your weight")
height = input("Enter your height")
intWeight = int(weight)
intHeight = float(height)
bmi = intWeight/(intHeight ** 2)
print(f"your BMI is {bmi}")

# Logical operators
# AND all conditions should be true
# OR any 1 condition should be true
# NOT should not be equal to given condition

# TRY AND EXCEPT
# TRY
# EXCEPT
# ELSE
# FINALLY

try:
    salary = int(input("enter your salary"))
except:
    print("there was an error")
else:
    print("you are eligible")
finally:
    print("thanks")

lp = int(input("enter a leap year to check"))
if lp % 4 == 0:
    if lp % 100 == 0:
        if lp % 400 == 0:
            print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is a leap year")
else:
    print("it is not a leap year")

