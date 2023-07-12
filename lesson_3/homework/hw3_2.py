# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

import re

my_string = 'Wombats are short-legged, muscular quadrupedal marsupials of the family Vombatidae that are ' \
            'native to Australia. Living species are about 1 m (40 in) in length with small, stubby tails ' \
            'and weigh between 20 and 35 kg (44 and 77 lb). They are adaptable and habitat tolerant, and are ' \
            'found in forested, mountainous, and heathland areas of southern and eastern Australia, ' \
            'including Tasmania, as well as an isolated patch of about 300 ha (740 acres) ' \
            'in Epping Forest National Park[2] in central Queensland.' \
            'Wombats dig extensive burrow systems with their rodent-like front teeth and powerful claws. ' \
            'One distinctive adaptation of wombats is their backward pouch. ' \
            'The advantage of a backward-facing pouch is that when digging, the wombat does not gather soil ' \
            'in its pouch over its young. Although mainly crepuscular and nocturnal, ' \
            'wombats may also venture out to feed on cool or overcast days. ' \
            'They are not commonly seen, but leave ample evidence of their passage, ' \
            'treating fences as minor inconveniences to be gone through or under.'


my_string_list = my_string.lower().split()

my_string_dict = {}

for i in my_string_list:
    k = i.strip('.,()[]')
    if k not in my_string_dict:
        my_string_dict[k] = 1
    else:
        my_string_dict[k] += 1


sorted_dict = dict(sorted(my_string_dict.items(), key=lambda x: x[1], reverse=True))
#print(sorted_dict)

ten_items = list(sorted_dict.items())[:10]
print(ten_items)
