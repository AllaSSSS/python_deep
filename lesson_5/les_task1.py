def task_1():
    my_list = map(int, input("введите строку: \n").split('/'))
    value_1, key_1, key_2, *value_2 = my_list
    my_dict = {key_1: value_1, key_2: tuple(value_2)}
    return my_dict


print(task_1())
