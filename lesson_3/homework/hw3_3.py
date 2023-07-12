# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

tourist_items = {
    'Палатка': 2.5,
    'Спальник': 1.5,
    'Фонарик': 0.2,
    'Котелок': 0.5,
    'Сухпаек': 2.0,
    'Кружка': 0.3,
    'Спички': 0.005,
    }

LOAD_CAP = 6.0
sum_weight = 0.0
items_to_take = []

for item, weight in tourist_items.items():
    if sum_weight + weight <= LOAD_CAP:
            items_to_take.append(item)
            sum_weight += weight

print(f'В рюкзак поместятся следующие вещи: {items_to_take}. Веc рюкзака составит: {sum_weight}')
