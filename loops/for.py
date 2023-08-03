name_list = ['dan', 'mike', 'micheal', 'faith', 'mary', 'rita']

for name in name_list:
    print(name)


# to get the index and element in one loop
for i, name in enumerate(name_list):
    print(name, i)

for i in range(0, 10):
    print(i)

print(list(range(0, 10)))

# adding even numbers between 0 and 101
sum = 0
for i in range(0, 101, 2):
    print(i)
    sum += i

print(sum)


# using break and continue
name_list2 = ['dan', 'mike', 'micheal', 'faith', 'mary', 'rita', 'peace', 'vicky', 'favor', 'blessing', 'terry']
for name in  name_list2:
    if name == 'faith':
        continue
    if name == 'vicky':
        break
    print(name)
print('done with loop')


animal_list = ['dog', 'goat', 'cow', 'chicken', 'hen', 'lion', 'tiger', 'wolf', 'tortoise', 'bear', 'fox']

for animal in animal_list:
    print(animal)
for animal in animal_list:
    if animal == 'wolf':
        break
    print(animal)
for animal in animal_list:
    if animal == 'cow':
        continue
    if animal == 'lion':
        continue
    if animal == 'bear':
        break
    print(animal)
    