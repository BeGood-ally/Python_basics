# task 1
'''def division(a,b):
    if b == 0:
        print('на ноль делить нельзя')
    if b != 0:
        return a/b
a = division(4,0)
print(a)'''

# task 2
'''def user_data(name, second_name, year, sity, email, tel):
    print('пользователь ' + name + ' ' + second_name + ' рожденный в '
          + year + ' году и проживающий в городе ' + sity + ' имеет email: ' + email + ' и телефон: ' + tel)
user_data(name = 'Иван', second_name = 'Сидоров', year = '1990',
          sity = 'Омск', email = 'Sidorov@mail.ru', tel = '89284857294')'''

# task 3
'''def my_func(a,b,c):
    if (a <= b and a <= c):
        return b + c
    if (b <= a and b <= c):
        return a + c
    else:
        return a + b

s = my_func(5,6,1)
print(s)'''

# task 4 with **
'''def my_func(x,y):
    if (y >= 0 or type(y) != int):
        print('"y" должен быть целым отрицательным числом')
    else:
        c = x ** y
        print(c)

my_func(2.0, -3)'''

# task 4 with cycle
'''def my_func(x,y):
    if (y >= 0 or type(y) != int):
        print('"y" должен быть целым отрицательным числом')
    else:
        i = -1
        j = x
        while(i > y):
            j = j * x
            i = i - 1
        return 1/j

a = my_func(2.0, -3)
print(a)'''

# task 5
'''arr_sum_all = 0
while True:
    numbs = input('введите числа, разделенные пробелами')
    arr = numbs.split()
    arr_sum = 0
    for ar in arr:
        if ar == 'x':
            arr_sum_all = arr_sum_all + arr_sum
            print(arr_sum_all)
            exit()
        else:
            arr_sum = arr_sum + int(ar)
    arr_sum_all = arr_sum_all + arr_sum
    print(arr_sum_all)'''

# task 6
def int_func(a):
    for j in a:
        if (ord(j) < 97 or ord(j) > 122):
            print('слово должно быть только из прописных букв латинского алфавита')
            return -1
        else:
            continue
    return a[0].upper() + a[1:len(a)]

def all_to_up_case(b):
    delay = 0
    for letter in b:
        if ord(letter) == 32:
            delay += 1
        else:
            continue
    if delay == 0:
        int_func(b)
    elif delay > 0:
        arr_b = b.split()
        i = 0
        arr_b_new = []
        for ev_b in arr_b:
            arr_b_new.append(int_func(ev_b))
        final_str = ' '.join(arr_b_new)
        print(final_str)

all_to_up_case('all from capital letter')

# task 6 with keyword "title"
stroak = 'каждое слово заглавное'
Stroak = stroak.title()
print(Stroak)