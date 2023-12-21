import yaml
import requests

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def get_login():
    path = data['path_login']
    post = requests.post(url=path, data={'username': data['username'], 'password': data['password']})
    if post.status_code == 200:
        return post.json()['token']


def get_post(token, owner = 'notMe'):
    path = data['path_post']
    #get = requests.get(url=path, params={'owner': 'notMe'}, headers={'X-Auth-Token': token})
    get = requests.get(url=path, params={'owner': owner}, headers={'X-Auth-Token': token})
    if get.status_code == 200:
        return get.json()


def create_post(token):
    path = data['path_post']
    create = requests.post(url=path, params={'title': "Pallas's cat", 'description': "This post is about the Pallas's "
        "cat, also known as manul", 'content': 'It is a small wild cat with long and dense light grey fur, and rounded '
        'ears set low on the sides of the head'}, headers={'X-Auth-Token': token})
    return create.status_code == 200


if __name__ == '__main__':
    token = get_login()
    print(get_post(token))
    print(create_post(token))




