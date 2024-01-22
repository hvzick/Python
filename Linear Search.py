arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
x = int(input("Enter an element to search in the List : "))
a = 0
for i in range(len(arr)):
    if arr[i] == x:
        a = 1
        break
if a == 1:
    print(f"Element {x} found at {i} index")
else:
    print(f"Element {x} not found")
