# for ii in range(1,10): # increments by 1
#     print(ii)
#
# print("---")
#
# for i in range(1,10,2): # increments by 2
#     print(i)
#
# print("---")
#
# sum1=0
# for s in range(1,101):
#     sum1 = s + sum1
# print(sum1)


# def add_odd_numbers():
#     a = 0
#     for i in range(1, 101,2):
#         a += i
#     return a
# op = add_odd_numbers()
# print(op)

def add_even_numbers(start, end):
    s = 0
    for i in range(start,end+1):
        if i % 2 == 0:
            s += i
    return s
op = add_even_numbers(1, 100)
print(op)