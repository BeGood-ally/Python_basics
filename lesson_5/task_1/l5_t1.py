while True:
    new_file = open('l5_t1.txt','a')
    add_str = input('введите строку, либо просто нажмите "enter" для завершения программы')
    if add_str == '':
        new_file.close()
        break
    else:
        new_file.write(add_str + '\n')
        new_file.close()