from script.ore import Ore
from random import choice, randint

def generate_ore():
    ore_list = ['Stone', 'Coal', 'Iron']
    ore = choice(ore_list)

    match ore:
        case 'Stone':
            return Ore('Stone', 10, 5, '../static/models/ores/stone.png')
        case 'Coal':
            return Ore('Coal', 15, 7, '../static/models/ores/coal.png')
        case 'Iron':
            return Ore('Iron', 30, 15, '../static/models/ores/iron.png')
