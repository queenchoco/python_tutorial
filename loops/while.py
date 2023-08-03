# printing numbers from 0 - 9
i = 0
while i < 10:
    print(i)
    i = i + 1


# adding numbers between 1 and 51
sum = 0
counter  = 1
while counter <= 50:
    sum = sum + counter
    counter = counter + 1

print(sum)

# adding even numbers between 1 and 101
sum = 0
counter = 2
while counter <= 100:
    if counter % 2 == 0:
        sum = sum + counter
    counter = counter + 1

print(sum)

name_list = ['dan', 'mike', 'micheal', 'faith', 'mary', 'rita']
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1