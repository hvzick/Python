def myfunc():
    print("hi i am hazik\n")
myfunc()
def multiply(x,y):
    z = x+y
    print(z)
multiply(5,3)
def me(name):
    print(f"hi {name}")
me("hazik")

def f(f,s):
   con = f+s
   return con

o = f("face", "book")
print(o)

def name(fname,lname):
    """"this function returns 2 value""" # this is called doc string
#     fn = fname.title()
#     ln = lname.title()
#     return f"{fn} {ln}"
#
# fname = input("enter first name")
# lname = input("enter last name")
#
# op = name(fname,lname)
# print(op)

def add1(n1, n2):
    return n1 + n2


def sub1(n1, n2):
    return n1 - n2


def mul1(n1, n2):
    return n1 * n2


def div1(n1, n2):
    return n1 / n2


n1 = int(input("What is the first number?"))
n2 = int(input("What is the second number?"))
op = input("Pick operation from this list (+,-,*,/)")


if op == "+":
    answer = add1(n1, n2)

elif op == "-":
    answer = sub1(n1, n2)

elif op == "/":
    answer = div1(n1, n2)

elif op == "*":
    answer = mul1(n1, n2)

print(f"{n1} {op} {n2} = {answer}")

