# Функция получает на вход строку из двух чисел через пробел. Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число. Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def task_3(current_str: str) -> dict[str, int]:


    my_list = current_str.split()
    my_begin = min(int(my_list[0]), int(my_list[1]))
    my_end = max(int(my_list[0]), int(my_list[1])) + 1
    my_dict = {}
    for item in range(my_begin, my_end):
        my_dict[chr(item)] = item
    return my_dict

