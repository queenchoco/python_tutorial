ass_list = [[1, 5, 'Hello', 6, 7, 9], 'Bat', 3, 7, 2, 'Cat', [1, 3, 10, '75', 17, 21, 7], 10, 19, [3, '25', 'Choco'], 0, '100']
ans_list = []

for item in ass_list:
    if type(item) is list:
        for i in item:
            if type(i) is int:
                if i not in ans_list:
                    ans_list.append(i)
    elif type(item) is int:
        if item not in ans_list:
            ans_list.append(item)

print(ans_list)