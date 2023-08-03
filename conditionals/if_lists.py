list_a = [1, 2, 3, 4, 5]
list_b = [1, 3, 5, 7, 9]

if 6 in list_a:
    print('List a contains 2')
else:
    print('List a does not contain 2')

animals = ['cat', 'dog', 'bat', 'chicken', 'rat']
if 'cat' in animals:
    print('Cat is an animal')

if 'iron' not in animals:
    print('Iron is not an animal')
else:
    print('Iron is an animal')

animal_a = 'rat'
print(animals)
if animal_a not in animals:
    animals.append(animal_a)
    print('New animal added to the animals list')
else:
    print('Animal is already in the animals list')

print(animals)


list_a = [1, 2, 3, 4]
list_b = [1, 2, '3', 4]


if list_a == list_b:
    print('List a is same with list b')
else:
    print('List a is not same with list b')