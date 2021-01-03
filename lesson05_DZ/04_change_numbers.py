with open('04_file_file', 'r', encoding='utf-8') as my_file:

    numbers = ["Один", "Два", "Три", "Четыре"]
    n = 0
    for line in my_file:
        name, sign, amount = line.split()
        name = numbers[n]
        n += 1
        strings = [name, sign, amount]

        with open('04_new_file.txt', 'a', encoding='utf-8') as my_file_w:
            if my_file_w.writable():
                my_file_w.writelines(' '.join(strings)+'\n')
            else:
                print("Cannot write")
