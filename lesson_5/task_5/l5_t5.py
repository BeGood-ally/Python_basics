from functools import reduce

while True:
    number = input('введите число или нажмите "enter" для завершения')
    if number != '':
        number_row = open('l5_t5.txt', 'a')
        number_row.write(number + ' ')
        number_row.close()
    if number == '':
        number_row = open('l5_t5.txt')
        count = number_row.read().split()
        summ = reduce(lambda x,y: int(x)+int(y), count)
        print(summ)
        break

#print(content)
