# 1

import requests
import os

search_hulk = 'search/Hulk'
search_captain_america = 'search/Captain_America'
search_thanos = 'search/Thanos'


def create_url(params):
    return "https://superheroapi.com/api/2619421814940190/" + params


def get_hero_id(search_hero):
    url = create_url(search_hero)
    resp = requests.get(url)
    return resp.json()['results'][0]['id']


def get_hero_intelligence(id):
    url = create_url(id + '/powerstats')
    resp = requests.get(url)
    return resp.json()['intelligence']


def get_most_hero_intelligence(hero_list):
    hero_name = ''
    hero_intelligence = 0
    for name, intelligence in hero_list.items():
        if int(intelligence) > int(hero_intelligence):
            hero_intelligence = intelligence
            hero_name = name
    return {hero_name: hero_intelligence}


hero_intelligence = {
    'Hulk': get_hero_intelligence(get_hero_id(search_hulk)),
    'Captain_America': get_hero_intelligence(get_hero_id(search_thanos)),
    'Thanos': get_hero_intelligence(get_hero_id(search_captain_america))
}

#print(get_most_hero_intelligence(hero_intelligence))


# 2


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        headers = {'Accept': 'application/json', "Authorization": self.token}
        params = {'path': file_path}
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', params=params, headers=headers)
        put_url = response.json().get('href')
        files = {'file': open(file_path, 'rb')}
        response = requests.put(put_url, files=files, headers=headers)
        print(response)


if __name__ == '__main__':
    uploader = YaUploader('')
    file_path = 'Ivan.txt'
    uploader.upload(file_path)
