# task 1
name = 'Vasiliu'
age = 3
lenght = 30.536
print(name, "is the cat, which", age, "years old, and which length is", lenght, "sm")

mark = input('введите марку вашего авто')
year = input('введите год выпуска вашей машины')
print(f'у вас машина марки {mark} {year}-го года выпуска')


# task 2
secs = input('введите произвольное количество секунд')
hours = int(secs) // 3600
minutes = int(secs) % 3600 // 60
seconds = int(secs) % 3600 % 60
print(f"В формате чч:мм:сс вы ввели следующее время: {hours}:{minutes}:{seconds}")
print("вы ввели: {0} часов: {1} минут: {2} секунд".format(hours, minutes, seconds))


# task 3
num = input("введите произвольное целое число от 1 до 10")
if (int(num) > 10):
    print("это больше десяти")
elif (int(num) < 1):
    print("это меньше одного")
else:
    num2 = num*2
    num3 = num*3
    print(int(num) + int(num2) + int(num3))

# task 4
big_num = input("введите число из двух и более цифр")
big_num_rest = 0
while (int(big_num) > 10):
    big_num_rest_new = int(big_num) % 10
    if (big_num_rest_new > big_num_rest):
        big_num_rest = big_num_rest_new
    big_num = int(big_num) // 10
if (int(big_num_rest) > int(big_num)):
    print(int(big_num_rest))
else:
    print(int(big_num))

# task 5
income = input("введите сумму выручки вашей фирмы за месяц")
outcome = input("введите сумму издежек вашей фирмы за этот же месяц")
if (int(outcome) > int(income)):
    print("ваша фирма терпит убытки, смените стратегию или станете банкротом")
elif (int(outcome) < int(income)):
    print("поздравляем, ваше дело приносит прибыль,\nа какое количество сотрудников в вашей фирме")
    people = input()
    print('''таким образом:
рентабельность вашей фирмы в этом месяце составила: %.2f
что в пересчете на каждого сотрудника примерно: %.2f''' % (int(income)/int(outcome), int(income)/int(outcome)/int(people)))
else:
    print("ваше положение стабильно, доход равен расходу")

# task 6
first_result = input("сколько пробежал спортсмен в первый день")
desire_result = input("сколько в итоге должен пробежать спортсмен")
i = 1
while (int(first_result) < int(desire_result)):
    first_result = float(first_result) + float(first_result)*0.1
    i += 1
print(f"спортсмен достигнет результата за количество дней равное: {i}")











