a = int(input("Введите число: "))
b = int(input("Введите степень числа: "))


def my_func(a, b):
    i = 1
    c = a
    while i < b:
        c = c * a
        i += 1
    return c


print(my_func(a, b))
