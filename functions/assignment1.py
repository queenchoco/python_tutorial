def add(num1, num2):
    return num1 + num2 

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2


# print(add(20, 30))
# print(sub(100, 30))
# print(mul(10, 15))
# print(div(75, 8))
# print(mod(75, 8))


def even_num(n):
    ans_num = []

    for i in range(2, n + 1, 2):
        ans_num.append(i)
    return ans_num

result = even_num(50)

print(result)

