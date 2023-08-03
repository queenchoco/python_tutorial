animal_list = ['dog', 'goat', 'cow', 'chicken', 'hen']
name_list = ['dan', 'mike', 'micheal', 'faith', 'mary']

another_list = [animal_list, name_list]
# print(another_list)
another_list[1][2]

for item in another_list:
    for name in item:
        print(name)

i = 0
while i < len(another_list):
    j = 0
    while j < len(another_list[i]):
        print(another_list[i][j])
        j += 1
    i += 1

i = 0
while i < len(another_list):
    for name in another_list[i]:
        print(name)
    i += 1


for item in another_list:
    i = 0
    while i < len(item):
        print(item[i])
        i += 1


for alp in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    for let in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(f'{alp}{let}')



ass_list = [[1, 5, 'Hello', 6, 7, 9], 'Bat', 3, 7, 2, 'Cat', [1, 3, 10, '75', 17, 21, 7], 10, 19, [3, '25', 'Choco'], 0, '100']