num1 = 10
num2 = 7

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
    print ('num1 is equal to num2')
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
    
number = input('pick a number from 1 to 200: ')
number = int(number)

if number < 1 or number > 200:
    print('number is not between 1 and 200')
elif number >= 1 and number <= 70:
    print('small number')
elif number >= 35 and number <= 90:
    print('medium number')
else:
    print('large numbers')


    