# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint
num = randint(0, 1000)

count = 1
shot = None

while count < 11:
    shot = int(input('Угадай число: '))
    if shot == num:
        print('Угадал!')
        break
    elif shot > num:
        print('Не угадал! Мое число меньше. Осталось попыток: ', 10 - count)
    else:
        print('Не угадал! Мое число больше. Осталось попыток: ', 10 - count)
    count += 1

print('Мое число:', num)

