from sheet2dict import Worksheet
from linkedlist import LinkedList

ws = Worksheet()
ws.xlsx_to_dict('games.xlsx')

games = ws.sheet_items
genres = ['Action', 'Adventure', 'RPG', 'Shooter', 'Puzzle', 'Platformer', 'Indie']
platforms = ['PC', 'Playstation', 'Xbox', 'Nintendo', 'Android', 'iOS']

linked_games = LinkedList()
names = []
for game in games:
    topics = list(game.values())
    linked_games.insert_beginning({topics[0]: [topics[0], topics[1], topics[2], topics[3], topics[4]]})
    names.append(topics[0])

del ws