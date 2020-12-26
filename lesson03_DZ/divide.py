def divide(var_1, var_2):
    try:
        devide_func = var_1 / var_2
        return devide_func
    except ZeroDivisionError:
        return


var_1 = int(input("Введите первое число: "))
var_2 = int(input("Введите второе число: "))
print(divide(var_1, var_2))
