import requests
from random import choice

class Pokemon:
    def __init__(self, nome, tipo, hp, level):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.level = level

link = 'https://testeBanco.jefersonvieira.repl.co'

req = requests.get(link)

pokedex = req.json()

listapokemons = []

for pokemon in pokedex:
    listapokemons.append(Pokemon(pokemon["nome"], pokemon["tipo"], pokemon["hp"], pokemon["level"]))

pokemon = choice(listapokemons)
print(f'''{pokemon.nome} - {pokemon.tipo} - {pokemon.hp}''')

