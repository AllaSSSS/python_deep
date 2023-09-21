# ------------------------------------------- 5 -----------------------------
# Напишите программу, которая решает квадратные уравнения
# даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

d = b ** 2 - 4 * a * c
x_1 = (-b + d ** 0.5) / (2 * a)
x_2 = (-b - d ** 0.5) / (2 * a)
if d > 0:
    result = f'У уравнения два корня: {x_1 = } и {x_2 = }'
elif d == 0:
    result = f'У уравнения один корень: {x_1 = }'
else:
    result = f'У уравнения два комплексных корня: {x_1 = } и {x_2 = }'

print(result)