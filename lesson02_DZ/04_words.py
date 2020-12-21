word_num = 0
word_list = input("Введите несколько слов: ")
split_word_list = word_list.split(" ")
while word_num < len(split_word_list):
    if len(split_word_list[word_num]) > 10:
        print(f"{word_num + 1} - {split_word_list[word_num][:10]}")
        word_num += 1
    else:
        print(f"{word_num + 1} - {split_word_list[word_num]}")
        word_num += 1
