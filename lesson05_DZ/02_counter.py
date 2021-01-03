file_ = open('02_file_file', 'r')
line = 0
for i in file_:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(word, 'слова')

print(line, 'строки')
file_.close()