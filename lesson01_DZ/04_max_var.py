lists1 = []
n = 0
var_1 = int(input("Введите число: "))
var_lenth = int(len(str(var_1)))
while n < var_lenth:
    var_01 = var_1 % 10
    lists1.insert(n, var_01)
    var_1 = var_1 // 10
    n += 1
print(max(lists1))
