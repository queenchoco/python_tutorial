# using a for loop to print all odd numbers between 0 and 51
# for i in range(1, 51, 2):
#    print(i)

numbers = [5, 11, 13, 6, 10]
square_numbers = []

for num in numbers:
   square_numbers.append(num * num)

print(square_numbers)