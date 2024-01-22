lp = int(input("Enter a leap year to check"))
if lp % 4 == 0:
    if lp % 100 == 0:
        if lp % 400 == 0:
            print(f"{lp} is a leap year")
        else:
            print(f"{lp} is not a leap year")
    else:
        print(f"{lp} is a leap year")
else:
    print(f"{lp} is not a leap year")
