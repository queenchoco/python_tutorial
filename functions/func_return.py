def add(num1, num2):
    return num1 + num2

add_list = []
add_list.append(add(12, 15))

# print(add_list)

def fib(n):
    fib_list = []
    if n < 1:
        return fib_list
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    for i in range(2, n): 
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(5))
print(fib(10))
print(fib(20))
