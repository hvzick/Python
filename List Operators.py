list = ['a', 'b', 'c', 'd', 'e']

print(list[0:1]) # Prints elements at index 0 only

print(list[:3]) # Prints elements upto index 2 only

print(list[2:]) # Prints elements from index 2 till end

print()
# REPLACING LISTS ELEMENTS WITH SLICING

mylist = [1,2,3,4,5]
print(mylist)
print(f"OLD LIST {mylist[1:3]}")
mylist[1:3] = 22,33
print(f"UPDATED LIST {mylist[1:3]}")
print(mylist)

# LIST CONCATENATING

print("### LIST CONCATENATING")
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)

# * OPERATOR
list4 = list1 * 4
print(list4)

# EXIST OPERATOR

check = 1 in list1
print(check) # RETURN TRUE IF ELEMENT EXISTS IN THE LIST OTHERWISE FALSE

print()
custom_list = [1,2,3,4,5,6,7,8,9,10]
print(custom_list[::-1])
print(dir(custom_list))