from os import system
from os import name as osname
from hashmap import *
from games import *
from findname import *

class Main:

    def __init__(self):
        self.start()

    def start(self):
        print('''Welcome to the Videogame Database v1.0b
1) Search by name
2) Search by rating (not implemented)
3) Search by release date (not implemented)
4) Search by genre (not implemented)
5) Search by platform (not implemented)''')
        opt = input('\nEnter a number from 1 to 5: ')

        if opt == '1':
            print(self.by_name())
    
    def by_name(self):
        name_map = HashMap(500)

        for game, values in games.items():
            name_map.assign(game, values)

        name = input('\nEnter a part of the name of the game you are lookng for: ')
        results = findname(name, names)
        
        if results == []:
            return '\nCouldn\'t find with any game matching your search query!'
        else:
            print('\nHere are the results for your search:')
            for game in results:
                value = name_map.retrieve(game)

                print(f'''
Name:         {value[0]}
Release date: {value[1]}
Rating:       {value[2]}
Genres:       {value[3]}
Platforms:    {value[4]}
''')










system('cls' if osname == 'nt' else 'clear')
main = Main()