# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

my_list = [330, 5, 1, 8, 2, 10, 12, 120]
print(my_list)
for j in range (len(my_list) - 1):
    for i in range (len(my_list) - 1 -j):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(my_list)