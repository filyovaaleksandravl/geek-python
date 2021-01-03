file_name = input('Введите имя файла: ')
file_name = open(file_name, 'w')
print("Для выхода введите пустую строку.")
while True:
    s = input()
    if s == '': break
    file_name.write(s + '\n')
file_name.close()
