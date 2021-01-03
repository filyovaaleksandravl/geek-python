with open('05_new_file.txt', 'w', encoding='utf-8') as my_file_w:
    if my_file_w.writable():
        my_file_w.writelines('1 2 3 5 6')
with open('05_new_file.txt', 'r', encoding='utf-8') as my_file_r:

    sum_var = 0
    for i in my_file_r:
        for j in i:
            if j !=' ':
                sum_var = sum_var + int(j)

    print(f"Сумма чисел в файле, равна: {sum_var}")
