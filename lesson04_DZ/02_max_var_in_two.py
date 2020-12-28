main_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
test_list = []
i = 1
while i < len(main_list):
    if main_list[i] > main_list[i + 1]:
        test_list.append(main_list[i])
        i += 2
    else:
        test_list.append(main_list[i + 1])
        i += 2


print(test_list)
