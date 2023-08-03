number_lists = [1, 3, 6, 10, 25, 8, 0, 2, 43]
oddnum_list = []

for num in number_lists:
    if num % 2 != 0:
        oddnum_list.append(num)

print(oddnum_list)

list1 = [10, 13, 14, 17, 2]
list2 = [0, 3, 4, 3, 5]
new_list = []

for i in range(len(list1)):
    new_list.append(list1[i] + list2[i])

print(new_list)