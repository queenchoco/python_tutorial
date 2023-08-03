alphabet_list = 'abcdefghijklmnopqrstuvwxyz'

for alphabet in alphabet_list:
    if alphabet == 'b':
        continue
    if alphabet == 'c':
        continue
    if alphabet == 'k':
        continue
    if alphabet == 'y':
        continue
    if alphabet == 'q':
        continue
    print(alphabet)


for alphabet in alphabet_list:
    if alphabet in ['b', 'c', 'k', 'y', 'q']:
        continue
    print(alphabet)
    