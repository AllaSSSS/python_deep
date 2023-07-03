# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

num = None

while True:
    num = int(input('Введите число от 1 до 999: '))
    if num > 1 and num < 999:
        break

if num > 1 and num < 10:
    print('Введена цифра.', num, 'в квадрате =', num ** 2)

elif num >= 10 and num < 100:
    dig_1 = num // 10
    dig_2 = num % 10
    print('Введено двузначное число. Произведение цифр =', dig_1 * dig_2)

else:
    dig_1 = num // 100
    dig_2 = num // 10 % 10
    dig_3 = num % 10

    if dig_3 == 0:
        print('Введено трехзначное число. Число в обратном порядке: ', dig_2, dig_1, sep='')
    else:
        print('Введено трехзначное число. Число в обратном порядке: ', dig_3, dig_2, dig_1, sep='')
