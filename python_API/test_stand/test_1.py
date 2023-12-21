import pytest
from check_post import get_post, create_post

id_check = 93393
desc_check = "This post is about the Pallas's cat, also known as manul"


def test_1(token):
    output = get_post(token)['data']
    print(output)
    res = []
    for item in output:
        res.append(item['id'])
    print(res)
    assert id_check in res


def test_2(token):
    assert create_post(token)
    output = get_post(token, owner='Me')['data']
    res = []
    for item in output:
        res.append(item['description'])
    assert desc_check in res