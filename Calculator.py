def addition(xL, yL):
    return xL + yL


def multiplication(xL, yL):
    return xL * yL


def division(xL, yL):
    return xL / yL


def subtraction(xL, yL):
    return xL - yL


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

s = input("Enter a symbol to perform the Arithmetic operation (+, -, *, /)")
output = 0
if s == '+':
    output = addition(x, y)

elif s == '*':
    output = multiplication(x, y)

elif s == '/':
    output = division(x, y)

elif s == '-':
    output = subtraction(x, y)

print(f"{x} {s} {y} = {output}")