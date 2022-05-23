# pip install requests
import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/charizard')

pokemonData = response.json()

for item in pokemonData['abilities']:
  print( item['ability']['name'] )
