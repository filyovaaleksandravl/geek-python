main_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
test_list = []
for x in main_list:
    if x not in test_list:
        test_list.append(x)
    else:
        test_list.remove(x)


print(test_list)
