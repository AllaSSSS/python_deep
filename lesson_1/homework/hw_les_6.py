# Проверка, является ли год високосным

year = int(input('Введите год в формате yyyy: '))
check1 = 4
check2 = 100
check3 = 400
check4 = 1582

if year % check1 != 0:
    print('Невисокосный')
elif year >= check4:
    if year % check2 == 0:
        if year % check3 == 0:
            print('Високосный')
        else:
            print('Невисокосный')
else:
    print('Високосный')
