subj = {}
with open('06_file_file', 'r', encoding='utf-8') as dicti:
    for line in dicti:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')
