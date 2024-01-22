drinks = ["pepsi","coca-cola","sprite"]
print(drinks[1]) # prints drink name at 1st index
print(drinks[-1]) # prints drink name from the ending of the list

drinks.append("sting") # adds it to the ending of the list
print(drinks[3])

list1 = [10, 10, 5, 15, 50, 50, 20]
i = list1.index(50)
list1[i] = 5
print(list1)

def count_words(p_list):
    x = 0
    for i in p_list:
        if len(i) >= 2 and i[0] == i[-1]:
            x = x+1
    return x

list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
op = count_words(list1)
print(op)

list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]
l3 = list()

o = list_one[1::2]
e = list_two[0::2]

l3.extend(o)
l3.extend(e)
print(l3)

custom_list = [10, 44, 57, 99, 11, 33, 84]
x = custom_list.pop(4)
custom_list.insert(2,x)
custom_list.append(x)
print(custom_list)


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(1,7000)
print(list1)


list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']

list1[2][1][2].insert(2,'h')
list1[2][1][2].insert(3,'i')
list1[2][1][2].insert(4,'j')

print(list1)
