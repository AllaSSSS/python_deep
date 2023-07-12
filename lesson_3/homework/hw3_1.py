# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 5, 24, 76, 5, 89, 24, 3, 100, 58, 89]

repeated_numbers = list()

for item in my_list:
    if my_list.count(item) > 1:
        repeated_numbers.append(item)

res_list = list(set(repeated_numbers))
print(res_list)
