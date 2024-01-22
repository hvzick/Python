def insert_first_element(my_list):
    first_element = int(input("Enter first number to insert in the list: "))
    my_list.insert(0, first_element)
    return my_list


def insert_at_last(my_list):
    last_element = int(input("Enter a number to insert in the list: "))
    my_list.append(last_element)
    return my_list


def delete_last_element(my_list):
    my_list.pop()
    return my_list


def delete_first_element(my_list):
    my_list.pop(0)
    return my_list


def insert_at_specific_position(my_list):
    position = int(input("Enter the index of the element: "))
    element = int(input("Enter the element to be inserted: "))
    my_list.insert(position, element)
    return my_list


def delete_at_specific_position(my_list):
    position = int(input("Enter the index of the element: "))
    element = int(input("Enter the element to be inserted: "))
    my_list.pop(position)
    return my_list


mylist = []
print("Enter 1 to to insert first element in the list")
print("Enter 2 to to insert at the end of the list")
print("Enter 3 to insert at a specific position in the list")
print("Enter 4 to delete the first element in the list")
print("Enter 5 to delete the last element in the list")
print("Enter 6 to delete at a specific position in the list")
print("Enter 0 to exit the program")
select = int(input())

while select != 0:


    if select == 1:
        insert_first_element(mylist)

    elif select == 2:
        insert_at_last(mylist)

    elif select == 3:
        insert_at_specific_position(mylist)

    elif select == 5:
        delete_last_element(mylist)

    elif select == 4:
        delete_first_element(mylist)

    elif select == 6:
        delete_last_element(mylist)


    elif select == 0:
        break

    print(mylist)
    print("Enter 1 to to insert first element in the list")
    print("Enter 2 to to insert at the end of the list")
    print("Enter 3 to insert at a specific position in the list")
    print("Enter 4 to delete the first element in the list")
    print("Enter 5 to delete the last element in the list")
    print("Enter 6 to delete at a specific position in the list")
    print("Enter 0 to exit the program")
    select = int(input())