from sheet2dict import Worksheet
from linkedlist import Node, LinkedList

ws = Worksheet()
ws.xlsx_to_dict('games.xlsx')

games = ws.sheet_items
genres = ['Action', 'Adventure', 'RPG', 'Shooter', 'Puzzle', 'Platformer', 'Indie']
platforms = ['PC', 'Playstation', 'Xbox', 'Nintendo', 'Android', 'iOS']
del ws

new_dict = {}
names = []
for game in games:
    topics = list(game.values())
    new_dict[topics[0]] = [topics[0], topics[1], topics[2], topics[3], topics[4]]
    names.append(topics[0])

games = new_dict
del new_dict