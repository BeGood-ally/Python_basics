# task 1
'''from sys import argv

script_name, first_param, second_param, third_param, fourth_param = argv
fourth_param = (first_param*second_param) + third_param

print('имя скрипта: ')
print('выработка в часах: ')
print('ставка в час: ')
print('премия: ')
print('заработная плата сотрудника: ')'''

# task 2
'''lis1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lis2 = [lis1[i] for i in range(len(lis1)) if (lis1[i] > lis1[i-1] and i >= 1)]
print(lis2)'''

# task 3
'''lis1 = [i for i in range(20,240) if (i % 20 == 0 or i % 21 == 0)]
print(lis1)'''

# task 4
'''lis1 = [1,2,2,3,7,7,8,4,1]
lis2 = []
i = 0
j = 0'''
'''while i < len(lis1):
    n = 0
    while j < len(lis1):
        if (lis1[i] == lis1[j] and i != j):
            n += 1
        j += 1
    if n == 0:
        lis2.append(lis1[i])
    i += 1'''
'''while i < len(lis1):
    n = 0
    while j < len(lis1):
        if (lis1[i] == lis1[j] and i != j):
            n += 1
            print(n)
        j += 1
    i += 1

#print(lis2)'''


'''for j in lis1:
    lis2 = [lis1[i] for i in range(len(lis1)) if lis1[i] != j]
print(lis2)'''
'''lis3 = []
u = 0
for i in range(len(lis1)):
    for j in range(len(lis1)):
        if (lis1[j] == lis1[i] and i != j):
            continue
        elif lis1[j] != lis1[i]:
            u = lis1[i]
    lis3.append(u)
print(lis3)'''

# task 5
'''from functools import reduce
lis1 = [i for i in range(100, 1001) if i % 2 == 0]
summ_lis1 = reduce(lambda x,y: x * y,lis1)
print(summ_lis1)'''

# task 6
'''from itertools import count
from itertools import cycle

for y in count(3):
    if y > 10:
        break
    else:
        print(y)

cyc = [4,8,6,8,3]
i = 0
for el in cycle(cyc):
    if i > 9:
        break
    print(el)
    i += 1'''

# task 7










