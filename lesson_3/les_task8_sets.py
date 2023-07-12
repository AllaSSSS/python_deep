# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться
#   на любое большее количество друзей.

friends_items = {
    'Друг1': ('Рюкзак', 'Палатка', 'Спальник', 'Фонарик'),
    'Друг2': ('Рюкзак', 'Палатка', 'Котелок', 'Кружка', 'Спички'),
    'Друг3': ('Рюкзак', 'Палатка', 'Спички', 'Складной стул'),
    }

all_items = set()

for key, value in friends_items.items():
    all_items.update(set(value))

#print(all_items)

common_items = (set.intersection(set(friends_items['Друг1']), set(friends_items['Друг2']), set(friends_items['Друг3'])))
print('У всех друзей есть: ', common_items)


print('Вещи, которые есть только у одного из друзей:')
for key, value in friends_items.items():
    unique_items = set(value)
    for name, item in friends_items.items():
        if name != key:
            unique_items.difference_update(set(item))
    print(key, unique_items)


print('Вещи, которых нет у одного из друзей: ')

for key, value in friends_items.items():
    two_friends_items = all_items.copy()
    for name, item in friends_items.items():
        if name != key:
            two_friends_items.intersection_update(set(item))
    two_friends_items.difference_update(set(value))
    if two_friends_items:
        print(key, two_friends_items)

