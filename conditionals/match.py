number = input('pick a number from 1 to 5: ')
number = int(number)

match number:
    case 1:
        print('Number is 1')
    case 2:
        print('Number is 2')
    case 3:
        print('Number is 3')
    case 4:
        print('Number is 4')
    case 5:
        print('number is 5')
    case _:
        print('Number is not between 1 and 5')