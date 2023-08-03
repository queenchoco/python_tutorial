import random
number = random.randint(-10, 10)

if number > 0:
    print(f'{number} is positive')
elif number == 0:
    print(f'{number} is zero')
else:
    print(f'{number} is negative')

number = random.randint(-10000, 10000)
last_digit = number % 10

if last_digit > 5:
    end_str = 'and is greater than 5'
elif last_digit == 0:
    end_str = 'and is 0'
elif last_digit < 6 and last_digit != 0:
    end_str = 'and is less than 6 and not 0'

print(f'Last digit of {number} is {last_digit} {end_str}')