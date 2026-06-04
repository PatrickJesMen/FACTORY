from script.ore import Ore
from random import choice

def generate_ore():
    ore_list = ['Stone', 'Coal', 'Iron']
    ore = choice(ore_list)

    match ore:
        case 'Stone':
            return Ore(name='Stone', health=10, cash=5, image='models/ores/stone.png')
        case 'Coal':
            return Ore(name='Coal', health=15, cash=7, image='models/ores/coal.png')
        case 'Iron':
            return Ore(name='Iron', health=30, cash=15, image='models/ores/iron.png')
