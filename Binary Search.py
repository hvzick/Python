def binary_search(arr, size, fdata):
    l = 0
    r = size - 1
    while l <= r:
        mid = round((l + r) / 2)
        if fdata == arr[mid]:
            return mid
        elif fdata > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def main():
    sorted_list = [15, 55, 67, 89, 113, 136, 178, 199, 213, 257, 378, 490, 515, 678, 790]
    data = int(input(f"Enter Data you want to search in this Array: {sorted_list} : "))
    size_of_list = len(sorted_list)
    binarySearchOutput = binary_search(sorted_list, size_of_list, data)
    if binarySearchOutput != -1:
        print(f"Element found at {binarySearchOutput} index")
    else:
        print("Element not found in the list")

if __name__ == "__main__":
    main()
