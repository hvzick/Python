def addition(x, y):
    return x + y


def multiplication(x, y):
    return x * y


def sum_of_list(listLocal):
    return sum(listLocal)


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

sumXY = addition(x, y)
print(f"Sum of {x} and {y} is {sumXY}")
mulXY = multiplication(x, y)
print(f"Product of {x} and {y} is {mulXY}")

list1 = [1, 2, 3, 4, 5]
s = 0
l = sum_of_list(list1)
print(f"The elements of list are {list1}")
print(f"The Sum of elements of the list is {l}")


