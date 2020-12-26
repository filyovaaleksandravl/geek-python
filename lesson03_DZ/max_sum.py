var_1 = int(input("Введите первый аргумент: "))
var_2 = int(input("Введите второй аргумент: "))
var_3 = int(input("Введите третий аргумент: "))
result_list = [var_1, var_2, var_3]


def my_func(result_list):
    result_list.sort()
    return result_list[1] + result_list[2]


print(my_func(result_list))
