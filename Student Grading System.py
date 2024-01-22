m = int(input("Enter Grades of a Student in Maths"))
s = int(input("Enter Grades of a Student in Science"))
ssc = int(input("Enter Grades of a Student in SSC"))
u = int(input("Enter Grades of a Student in Urdu"))
e = int(input("Enter Grades of a Student in English"))

percentage = (m+s+ssc+u+e)/5

if percentage <= 30:
    print(f"Percentage = {percentage}  : Your Grade is D, You Have FAILED")

if percentage >= 30 < 50:
    print(f"Percentage = {percentage}  : Your Grade is D")

if percentage >= 50 < 70:
    print(f"Percentage = {percentage}  : Your Grade is C")

if percentage >= 70 < 80:
    print(f"Percentage = {percentage}  : Your Grade is B")

if percentage >= 80 < 90:
    print(f"Percentage = {percentage}  : Your Grade is A")

if percentage >= 90 <= 100:
    print(f"Percentage = {percentage}  : Your Grade is A+")
