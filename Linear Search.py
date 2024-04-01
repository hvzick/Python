def linear_search():
    arr = [100, 27, 3654, 45, 544, 63, 76, 8, 96, 790]
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

linear_search()