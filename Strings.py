# adding int characters of a string
def sum_of_two_digits():
    a = input("Enter two digit number: ")
    x = int(a[0]) + int(a[1])
    return x

print(sum_of_two_digits())

# String Traversal

str = "hazik"
i = 0

for i in range(len(str)):
    print(str[i])

# String Reverse Traversal

str1 = "Python"
i = -1
while i >= -len(str1):
    print(str1[i])
    i = i-1


# Counting a Letter in a string

def count_letter(word,letter):
     c = 0
     for a in word:
         if a == letter:
             c = c+1
     return c

op = count_letter("Learning Python", "n")
print(op)


def first_last_characters(word):
    if len(word)<2:
        return ''
    x = word[0:2]
    y = word[-2:]
    return x+y


print(first_last_characters('appmillers'))

# How to capitalise first letter
myName = "hazik"
print(myName.capitalize())

# How to change letter to upper case
print(myName.upper())

# How to change letter to lower case
print(myName.lower())

# shows methods which we can use on a string
help(dir(myName))

# used to replace a character in a string
print(myName.replace('h', 'f'))

