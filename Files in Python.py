# for writing onto a file
# name = input("Whats your name: ")
# need to open and close file every time
# file = open('names.txt', 'a')
# file.write(f"{name}\n")
# file.close()

# no need to close file every time this does it automatically
# name = input("Whats your name: ")
# with open('names.txt', 'a') as file:
#     file.write(f"{name}\n")


# for reading a file

# with open('names.txt', 'r') as file:
#     lines = file.readlines()
#
# for line in lines:
#     print("Hello ", line.rstrip())
# with open('names.txt', 'r') as file:
#     for line in sorted(file):
#         print("Hello, ", line.rstrip())

### CSV stands for comma seperated values
with open('names.csv', 'r') as file:
    for line in sorted(file):
        name, value = line.rstrip().split(",")
       #print(f"Name: {name}, Value: {value}")
        data = {'name' : name, 'value' : value}
        data.append(data)

for d in data:
    print(f"Name: {name}, Value: {value}")