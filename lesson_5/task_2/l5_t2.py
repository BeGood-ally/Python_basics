file1 = open('l5_t2.txt')
i = 0
words = []
for line in file1:
    w = line.split()
    words.append(len(w))
    i += 1
print('количество строк в файле ' + str(i))
j = 1
for word in words:
    print('количество слов в строке ' + str(j) + ' равно ' + str(word))
    j += 1

