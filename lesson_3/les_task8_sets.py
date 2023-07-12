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

common_items = (set.intersection(set(friends_items['Друг1']), set(friends_items['Друг2']), set(friends_items['Друг3'])))
print(common_items)

friend1_items = set(friends_items['Друг1'])
friend2_items = set(friends_items['Друг2'])
friend3_items = set(friends_items['Друг3'])

unique_items = set()
for i in friend1_items:
    if i not in friend2_items and i not in friend3_items:
        unique_items.add(i)
for i in friend2_items:
    if i not in friend1_items and i not in friend3_items:
        unique_items.add(i)
for i in friend3_items:
    if i not in friend1_items and i not in friend2_items:
        unique_items.add(i)
print(unique_items)

#print(set.difference(set(friends_items['Друг1']), set(friends_items['Друг2']), set(friends_items['Друг3'])))

#for item in friends_items.values():
#    unique_items.update(set(item).difference(all_items))

