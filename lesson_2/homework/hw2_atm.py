# Напишите программу банкомат.

#   Начальная сумма равна нулю
#   Допустимые действия: пополнить, снять, выйти
#   Сумма пополнения и снятия кратны 50 у.е.
#   Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#   После каждой третей операции пополнения или снятия начисляются проценты - 3%
#   Нельзя снять больше, чем на счёте
#   При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
#   Любое действие выводит сумму денег

balance = 0
count = 0

while True:

    if balance > 50000000:
        balance = balance - balance * 0.1

    choice = int(input('Пополнить = 1, \n'
                    'Снять = 2, \n'
                    'Выйти = 3. \n'
                    'Выберите действие: '))

    if choice == 1:
        deposit = int(input('Введите сумму пополнения: '))
        if deposit % 50 == 0:
            balance = balance + deposit
            count += 1
        else:
            print(f'Сумма должна быть кратна 50! Текущая сумма: {balance}')

    elif choice == 2:
        withdraw = int(input('Введите сумму снятия: '))
        if withdraw > balance:
            print('Нельзя снять больше, чем на счете!')
        elif withdraw % 50 == 0:
            if withdraw * 0.015 < 30:
                balance = balance - withdraw - 30
            elif withdraw * 0.015 > 600:
                balance = balance - withdraw - 600
            else:
                balance = balance - withdraw - withdraw * 0.015
            count += 1
        else:
            print(f'Сумма должна быть кратна 50! Текущая сумма: {balance}')

    elif choice == 3:
        print(f'Сумма на счете: {balance}. До свидания!')
        break

    else:
        print('Введите цифру, соответствующую нужной операции!')

    if count == 3:
        balance = balance + balance * 0.03
        print(f'Вам начислен бонус!')
        count = 0

    print(f'Сумма на счете: {balance}')











