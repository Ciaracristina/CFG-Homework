import requests

pokemon_numbers = [5, 9, 13, 21, 38, 52]

for pokemon_number in pokemon_numbers:
    print()

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

    response = requests.get(url)
    pokemon = response.json()

    print(pokemon['name'].upper())

    moves = pokemon['moves']

    for move in moves:
        print(move['move']['name'])
