import requests

url = 'https://api.pokemonbattle.ru/v2'
Token = 'f93dfec59fdda8fc32315edbfbecbed9'
Header = {'Content-Type': 'application/json',
          'trainer_token': Token}

body_registration = {"trainer_token": Token,
    "email": "masha_qa@mail.ru",
    "password": "Iloveqa12"}

body_reg_confirmation = {"trainer_token": Token}

body_create_pokemon = {"name": "Хаги Ваги",
                       "photo_id": -1}

body_change_pokemon = {"pokemon_id": "69640",
    "name": "Хаги Ваги возвращается",
    "photo_id": 2}

body_add_pokeball = {"pokemon_id": "69640"}


response = requests.post(url=f'{url}/trainers/reg', headers = Header, json = body_registration)
print(response.text)

response_reg-confirmation = requests.post(url = f'{url}/trainers/confirm_email', headers=Header, json=body_reg_confirmation)
print(response.text)

response_create_pokemon = requests.post(url=f'{url}/pokemons', headers=Header, json = body_create_pokemon)
print(response_create_pokemon.text)

pokemon_id = response_create_pokemon.json()["id"]
print(pokemon_id)

response_change_pokemon = requests.put(url=f'{url}/pokemons', headers=Header, json = body_change_pokemon)
print(response_change_pokemon.json)

response_add_pokeball = requests.post(url=f'{url}/trainers/add_pokeball', headers=Header, json = body_add_pokeball)
print(response_add_pokeball.text)

response_list_pokemons = requests.get(url=f'{url}/pokemons?trainer_id=4634&status=1', headers=Header)
print(response_list_pokemons.text)