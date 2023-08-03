def print_alp():
    for alp in 'abcdefghijklmnopqrstuvwxyz':
        if alp in ['a', 'c', 'z', 'q']:
            continue
        print(alp)

# print_alp()

def print_name(n):
    for i in range(n):
        print('Hello World!')


# print_name(20)
total  = 20

def add(num1, num2):
    total = num1 + num2
    print(f'The result of {num1} + {num2} is {total}')

# print(total)
# add(10, 20)
# add(100, 26776)