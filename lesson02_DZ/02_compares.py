var_lists = []
key = 0
lists_lenth = int(input("Введите код-во элементов: "))
for i in range(0, lists_lenth):
    var_lists_add = input("Введите элемент: ")
    var_lists.append(var_lists_add)
print(var_lists)
if lists_lenth % 2 == 0:
    while key < lists_lenth:
        var_lists[key], var_lists[key + 1] = var_lists[key + 1], var_lists[key]
        key = key + 2
else:
    while key < lists_lenth-1:
        var_lists[key], var_lists[key + 1] = var_lists[key + 1], var_lists[key]
        key = key + 2

print(var_lists)
