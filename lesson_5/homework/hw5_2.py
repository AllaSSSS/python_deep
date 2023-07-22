# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


import os

def return_tuple(path):
    no_ext, ext = os.path.splitext(path)
    return (os.path.dirname(path), os.path.basename(no_ext), ext)


my_string = '/Thecode/Media/статья.txt'
print(return_tuple(my_string))