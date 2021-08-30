with open('l5_t4.txt') as eng_nums:
    e_numbers = []
    for line in eng_nums:
        e_number = line.split()
        e_numbers.append(e_number)
    r_numbers = ['Один','Два','Три','Четыре']
    for i in range(0,4):
        e_numbers[i][0] = r_numbers[i]
rus_nums = open('l5_t4(r).txt', 'a', encoding='utf-8')
for i in range(0,4):
    rus_nums.write(' '.join(e_numbers[i]) + '\n')
rus_nums.close()


