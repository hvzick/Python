# continue is used to skip current iteration in a loop when condition is met
# break us used to get out of the loop when condition is met
# for i in range(1,101):
#     if i % 2 == 0:
#         continue # skips even numbers
#     else:
#         print(i)
#
# print("---")
#
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)
# print("THE END")
#


# def numbers_divisible_byfive(p_list):
#     for i in p_list:
#         if i % 5 == 0:
#             print(i)
#         if i > 130:
#             break
#     print("STOP")
#
# p_list = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
# numbers_divisible_byfive(p_list)

# def factorial(p_num):
#     a = 1
#     if p_num < 0:
#         return "Factorial does not exist for negative numbers"
#     elif p_num == 0:
#         return "The factorial of 0 is 1"
#     else:
#         for num in range(1,p_num+1):
#             a = a * num
#         return f"The factorial of {p_num} is {a}"
#
# print(factorial(5))

# def check_for_float(p_input):
#     try:
#         val = float(p_input)
#         return val
#     except ( ValueError, TypeError):
#         print("Error, please enter numeric input")
#         return False
#
# count = 0
# total = 0.0
# average = 0.0
#
# while True:
#     input_number = input("Enter a number: ")
#     if input_number == "done":
#         break
#
#     number = check_for_float(input_number)
#     if not number:
#         continue
#
#     count +=1
#     total - total + number
# if count !=0:
#     average = total / count
# print(total,count,average)


def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return False

in1 = input("Enter a number: ")
number = check_for_float(in1)
big = number
s = number

while True:
    input_number = input("Enter a number: ")
    if input_number == "done":
        break

    number = check_for_float(input_number)
    if not number:
        continue

    if number > big:
        big = number
    elif number < s:
        s = number
print(f"Maximum number: {big}, Minimum number: {s}")
