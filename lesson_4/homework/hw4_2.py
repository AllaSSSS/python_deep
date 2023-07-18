# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

import typing


def args_to_dict(**kwargs):

    res_dict = {}

    for key, val in kwargs.items():
        if isinstance(val, typing.Hashable):
            res_dict[val] = key
        else:
            res_dict[str(val)] = key
    return res_dict

#return {val: name for name, val in kwargs.items()}


print(args_to_dict(a='Hello', b='World', c='!', d=[1, 2, 3], e=[2, 'y'], f=True, g=0.002))

