# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

HEX: int = 16

num: int = int(input('Введите число: '))

test_num = num
result: str = ''
while test_num > 0:
    result = str(test_num % HEX) + result
    test_num //= HEX

print(f'For {num}, result = {result}')
print(f'Check with hex: {hex(num)[2:]}')
