# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

HEX = 16
hex_system = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

num = int(input('Введите число: '))

test_num = num
result: str = ''
while test_num > 0:
    result = hex_system[test_num % HEX] + result
    test_num //= HEX

print(f'For {num}, result = {result}')
print(f'Check with hex: {hex(num)[2:]}')