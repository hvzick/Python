def factorial(n):
     if n == 0 or n == 1:
         return 1
     else:
         return n * factorial(n-1)

def main():
    user_input = int(input("Enter a number to find its Factorial: "))
    output = factorial(user_input)
    print(f"The Factorial of {user_input} is {output}")

if __name__ =="__main__":
    main()