# Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем
# каталоге, читает его и выводит два слова: наиболее часто встречающееся из тех, что имеют размер
# более трех символов, и наиболее длинное слово на английском языке.
#
# В файле ожидается смешанный текст на двух языках — русском и английском.

file_name = input()
with open(file_name, encoding = 'utf8') as myFile:
    for line in myFile:
        print(line)

punctuation = '.,:;?!-_)(%*"<>/[]{}'
summary = ''
def delete_punctuation(char):
    if char in punctuation:
        return ''
    else:
        return char

with open(file_name, encoding = 'utf8') as myFile:
    for line in myFile:
        for char in line:
            summary += delete_punctuation(char)
            summary = summary.replace('\n', ' ')
            summary = summary.lower()

with open('output.txt', 'w', encoding = 'utf8') as myFile:
    myFile.write(summary)

with open('output.txt', 'rt', encoding = 'utf8') as myFile:
    summary = myFile.readlines()
    summary = summary[0].split()
    most_often = None
    count = 0
    max_count = 0
    for k in range(len(summary)):
        if len(summary[k]) > 3:
            count = summary.count(summary[k])
            if count >= max_count:
                max_count = count
                most_often = summary[k]
    en_alpha = 'abcdefghijklmnopqrstuvwxyz'
    eng_words = []
    count = 0
    for i in range(len(summary)):
        for j in range(len(summary[i])):
            if summary[i][j] in en_alpha:
                count +=1
                if count == len(summary[i]):
                    eng_words.append(summary[i])
                    count = 0
    max_len = 0
    longest_word = None
    for i in range(len(eng_words)):
        if len(eng_words[i]) >= max_len:
            max_len = len(eng_words[i])
            longest_word = eng_words[i]

    print(f'Наиболее часто встречающееся слово из тех, что имеют размер более трех символов - "{most_often}"')
    print(f'Наиболее длинное слово на английском языке - "{longest_word}"')

myFile.close()