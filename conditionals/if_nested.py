import random
number = random.randint(0, 1000)

if number % 2 == 0:
    print(f'{number} is even ', end='')
    if number % 4 == 0:
        print('and divisible by 4')
    else:
        print('and not divisible by 4')
          