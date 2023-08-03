x = 9
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')
print('Outside if statement')

num1 = 10
num2 = 10

# greater than
if num1 > num2:
    print('num1 is greater than num2')
else:
    print('num1 is not greater than num2')

# less than
if num1 < num2:
    print('num1 is less than num2')
else:
    print('num1 is not less than num2')

# equal to
if num1 == num2:
    print('num1 is equal to num2')
else:
    print('num2 is not equal to num1')

# greater than or equal to
if num1 >= num2:
    print('num1 is greater than or equal to num2')
else:
    print('num2 is not greater than or equal to num1')

# less than or equal to
if num1 <= num2:
    print('num1 is less than or equal to num2')
else:
    print('num2 is not less than or equal to num1')

# not equal to
if num1 != num2:
    print('num1 is not equal to num2')
else:
    print('num2 is equal to num1')

number = input('Pick a number between 1 and 100: ')
number = int(number)

if number < 1 or number > 100:
    print('Number is not between 1 and 100')
elif number >= 1 and number <= 30:
    print('Small number')
elif number >= 31 and number <= 70:
    print('Medium number')
else:
    print('Large number')

if not number > 5:
    print('Hehehehehehehehehehe')