import pytest
from lesson1 import test_func


folder_in = '/home/alla/folder_in'
folder_out = '/home/alla/folder_out'
folder_ex = '/home/alla/folder_ex'


def test_step_1():
    assert test_func(f' cd {folder_in}; 7z a {folder_out}/archive_1', 'Everything is Ok')

# def test_step_2():
#     assert test_func(f' cd {folder_out}; 7z d archive_1', 'Everything is Ok')

def test_step_3():
    assert test_func(f' cd {folder_out}; 7z l archive_1.7z', 'file_1.txt')
    assert test_func(f' cd {folder_out}; 7z l archive_1.7z', 'file_2.txt')
    assert test_func(f' cd {folder_out}; 7z l archive_1.7z', 'file_3.txt')

def test_step_4():
    assert test_func(f' cd {folder_out}; 7z x archive_1.7z', 'Everything is Ok')

if __name__ == '__main__':
    pytest.main('[-vv]')