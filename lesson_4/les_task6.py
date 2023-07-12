# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
# Если нижняя граница меньше нуля, суммируем от начала. Если верхняя граница больше длины списка, до конца.

from random import randint

my_list = [randint (1, 10) for i in range (10)]
print(my_list)
a, b = map(int, input("Ввести 2 числа через пробел: ").split())
if a > b:
    a, b = b, a
if a < 0:
    a = 0
if b > len(my_list):
    b = len(my_list)
result = sum(my_list[a:b+1])
print(result)