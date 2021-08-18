# task 1
'''arr1 = [2, 'f', True, 'false', 4.6]
for i in arr:
    print(type(i))

# task 2
arr2 = []
while True:
    inp = input('введите число либо слово "end"')
    if inp == 'end':
        break
    else:
        arr2.append(inp)
print(arr2)
i = 0
while i < len(arr2):
    if i%2 != 0:
        temp = arr2[i]
        arr2[i] = arr2[i - 1]
        arr2[i - 1] = temp
    i += 1
print(arr2)'''

# task 3 with list
'''month = []
season = []
while True:
    mon = input('введите номер месяца либо "0" для выхода')
    if (0 < int(mon) <= 2 or int(mon) == 12 ):
        month.append(mon)
        season.append('зима')
    elif (2 < int(mon) < 6):
        month.append(mon)
        season.append('весна')
    elif (6 <= int(mon) <= 8):
        month.append(mon)
        season.append('лето')
    elif (8 < int(mon) < 12):
        month.append(mon)
        season.append('осень')
    elif int(mon) == 0:
        break
    else:
        print("месяца с таким номером нет")
        continue
print(month)
print(season)'''

# task3 with dict
'''month = ()
season = {}
while True:
    mon = input('введите номер месяца либо "0" для выхода')
    seas = ''
    if (0 < int(mon) <= 2 or int(mon) == 12):
       seas = 'зима'
    elif (2 < int(mon) < 6):
        seas = 'весна'
    elif (6 <= int(mon) <= 8):
        seas = 'лето'
    elif (8 < int(mon) < 12):
        seas = 'осень'
    elif int(mon) == 0:
        break
    else:
        print("месяца с таким номером нет")
        continue
    season.setdefault(mon, seas)
print(season)'''

# task 4
'''str1 = input("введите строку из нескольких слов")
j = 1
str2 = str1.split(' ')
for i in str2:
    if i != '':
        print(str(j) + "." + i[0:10])
        j += 1
    else:
        continue

#task 5
r = [9,7,7,4,2]
while True:
    new_dig = input('введите число или "exit"')
    if new_dig == "exit":
        break
    else:
        i = 0
        while i < len(r):
            if int(new_dig) >= r[0]:
                r.insert(0, int(new_dig))
                break
            elif int(new_dig) > r[i] and int(new_dig) <= r[i-1]:
                r.insert(i, int(new_dig))
                break
            elif int(new_dig) < r[-1]:
                r.append(int(new_dig))
                
            i += 1break
        print(r)'''






