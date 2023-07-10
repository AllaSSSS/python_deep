# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

fraction_1 = str(input('Введите первую дробь в формате a/b: '))
fraction_2 = str(input('Введите вторую дробь в формате a/b: '))

def define_enumerator_and_denominator(source_string):
    enumerator, denominator = source_string.split(sep='/')
    return int(enumerator), int(denominator)

enumerator1 = define_enumerator_and_denominator(fraction_1)[0]
enumerator2 = define_enumerator_and_denominator(fraction_2)[0]
denominator1 = define_enumerator_and_denominator(fraction_1)[1]
denominator2 = define_enumerator_and_denominator(fraction_2)[1]

sum = str(f'{(enumerator1 * denominator2 + denominator1 * enumerator2)}/{(denominator1 * denominator2)}')
product = str(f'{enumerator1 * enumerator2}/{denominator1 * denominator2}')

print('Сумма дробей =', sum)
print('Произведение дробей =', product)
