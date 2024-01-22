# name = 'Hazik'
# print('Hey %s' %name)
# name2 = 'Bot'
# print('Hey %s,My name is %s' %(name, name2))
#
# print("Hey %(name)s,My name is %(name2)s" %{'name':name,'name2': name2})



def print_pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*", end = ' ')
        print()
    for f in range(n, 0, -1):
        for ff in range(0, f-1):
            print('*', end = ' ')
        print()

print_pattern(6)

# def square_list(p_list):
#     for i in range(0, len(p_list)):
#         p_list[i] = p_list[i] * p_list[i]
#     return p_list
#
# custom_list = [1,2,3,4,5]
# print(square_list(custom_list))