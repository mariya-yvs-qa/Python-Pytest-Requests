import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
Token = 'f93dfec59fdda8fc32315edbfbecbed9'
Header = {'Content-Type': 'application/json','trainer_token': Token}
trainer_id = '4634'

def test_status_code():
    response = requests.get(url= f'{url}/trainers', params={'trainer_id': trainer_id})
    assert response.status_code==200

def test_part_of_response():
    response_trainer_name = requests.get(url= f'{url}/trainers', params={'trainer_id': trainer_id})
    assert response_trainer_name.json()["data"][0]["trainer_name"] == 'Sakura'