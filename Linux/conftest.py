import os
import datetime
import pytest
import yaml
from lesson1 import test_func

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope='class')
def make_folders():
    return test_func(f'mkdir -p {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ex")}', "")


@pytest.fixture(scope='class')
def delete_folders():
    yield
    return test_func(f'rm -rf {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ex")}', "")


@pytest.fixture(scope='class')
def make_files():
    return test_func(f'cd {data.get("folder_in")}; touch file_1.txt file_2.txt file_3,txt', "")


@pytest.fixture(autouse=True)
def run_after_each(request):
    with open("stat.txt", "a") as file1:
        # Writing data to a file
        folder_in = data.get("folder_in")
        if os.path.exists(folder_in):
            sz = os.stat(folder_in).st_size
        else:
            sz = 0
        with open("/proc/loadavg", "r") as loadavg:
            load = loadavg.read()
        file1.write(f'{datetime.datetime.now()} {request.node.name} {len(data)} size= {sz} {load}')
