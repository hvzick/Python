my_dictionary1 = {"Hazik": "My name is Hazik"}

my_dictionary2 = {
    "Faizan": "He is my classmate",
    "Atif": "He is my cousin",
    "Mehnoor": "She is my sister",
    21048112060: "This is my enrollment no."
}
print(my_dictionary1)
print(my_dictionary2)
print(my_dictionary1["Hazik"])
print(my_dictionary2[21048112060])

my_dict = {}
print(my_dict)
my_dict["Zero"] = 'It is a number'
my_dict["Java"] = 'It is a programming language'
print(my_dict)
my_dict["Zero"] = 'Updated value of zero'
print(my_dict)


def generate_dictionary(a):
    my_dictionary = dict()
    for i in range(1, a + 1):
        my_dictionary[i] = i * i
    return my_dictionary


op = generate_dictionary(5)
print(op)

for i in my_dictionary2:
    print(my_dictionary2[i])

my_dictionary2.pop("Faizan")
print(my_dictionary2)

dictt = {"hello":"world"}
print(dictt.pop("helloo","this key doesnt exist"))
print(dictt)

dicttt = {
    1:"one",
    2:"two",
    3:"three"
}

print(2 in dicttt)
# it will return true because 1 is present in the dicttt but it doesnt check for key value ex
print("one" in dicttt)


d = {}
for n in dicttt:
    d[n] = dicttt[n]

for n in d:
    print(n,d[n])

dict1 = {
    'faIk' : "name",
    'aTif' : "csn",
}

import re

def camel_to_title_case(key):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', key).title()

def camel_to_title_case_dict(input_dict):
    result_dict = {}
    for key, value in input_dict.items():
        title_case_key = camel_to_title_case(key)
        result_dict[title_case_key] = value
    return result_dict

# Example usage:
input_dict = {
    'camelCasedKey1': 'value1',
    'anotherCamelCasedKey': 'value2',
    'yetAnotherKey': 'value3'
}

result_dict = camel_to_title_case_dict(input_dict)
print(result_dict)

