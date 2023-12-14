import pytest
from lesson1 import test_func
import yaml


with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


# @pytest.mark.usefixtures('make_folders', 'make_files', 'delete_folders')
@pytest.mark.usefixtures('make_folders', 'make_files')
class TestSem:

    def test_step_1(self):
        assert test_func(f' cd {data.get("folder_in")}; 7z a -t{data.get("arch_type")} {data.get("folder_out")}/archive_1', 'Everything is Ok')

    def test_step_2(self):
        assert test_func(f' cd {data.get("folder_out")}; 7z d -t{data.get("arch_type")} archive_1', 'Everything is Ok')

    def test_step_3(self):
        assert test_func(f' cd {data.get("folder_out")}; 7z l -t{data.get("arch_type")} archive_1.{data.get("arch_type")}', 'file_1.txt')
        assert test_func(f' cd {data.get("folder_out")}; 7z l -t{data.get("arch_type")} archive_1.{data.get("arch_type")}', 'file_2.txt')
        assert test_func(f' cd {data.get("folder_out")}; 7z l -t{data.get("arch_type")} archive_1.{data.get("arch_type")}', 'file_3.txt')

    def test_step_4(self):
        assert test_func(f' cd {data.get("folder_out")}; 7z x -t{data.get("arch_type")} archive_1.{data.get("arch_type")}', 'Everything is Ok')


if __name__ == '__main__':
    pytest.main('[-vv]')