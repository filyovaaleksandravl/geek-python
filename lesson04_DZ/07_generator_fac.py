from math import factorial


def fact(n: int):
    for i in range(1, n + 1):
        yield factorial(i)


value = int(input("Введите число: "))
for el in fact(value):
    print(el)
