from os import system
from os import name as osname
from hashmap import *
from games import *
from findname import *
from ratingmap import *

class Main:

    def __init__(self):
        self.start()

    def get_option(self):
        print('''
1) Search by name
2) Search by rating (not implemented)
3) Search by release date (not implemented)
4) Search by genre (not implemented)
5) Search by platform (not implemented)''')

        return input('\nEnter a number from 1 to 5: ')
    
    def cont(self):
        query = input('Would you like to make another search? Enter y/n: ')
        if query == 'y':
            system('cls' if osname == 'nt' else 'clear')
            print('What would you like to do now?')
            opt = self.get_option()

            if opt == '1':
                self.by_name()
            if opt == '2':
                self.by_rating()
        
        else:
            print('\nThank you for using VGdb!')

    def start(self):
        print('Welcome to the VGdb v1.0b')
        opt = self.get_option()

        if opt == '1':
            self.by_name()
        if opt == '2':
            self.by_rating()
    
    def by_name(self):
        name_map = HashMap(500)
        for game, values in games.items():
            name_map.assign(game, values)

        name = input('\nEnter a part of the name of the game you are lookng for: ')
        name_list = names.copy()
        results = []
        results = findname(name, name_list, matching_list=results)
        
        if results == []:
            return '\nCouldn\'t find with any game matching your search query!'
        else:
            print('\nHere are the results for your search:')
            for game in results:
                value = name_map.retrieve(game)

                print(f'''
        Name: {value[0]}
Release date: {value[1]}
      Rating: {value[2]}
      Genres: {value[3]}
   Platforms: {value[4]}
''')

        self.cont()

    def by_rating(self):
        rating_map = RatingMap()
        for game, values in games.items():
            if values[2] != 'None':
                rating_map.assign(values[2], values)
        
        rating = input('''\nThe program will return a list of 10 games that have equal or higher metacritic score.
Pick a rating from 1-100: ''')

        list_of_games = rating_map.retrieve(rating)
        current_list = len(list_of_games)
        remaining = 10 - current_list
        if list_of_games != []:
            for i in range(current_list):
                print(f'''
        Name: {list_of_games[0][0]}
Release date: {list_of_games[0][1]}
      Rating: {list_of_games[0][2]}
      Genres: {list_of_games[0][3]}
   Platforms: {list_of_games[0][4]}
''')

        while remaining > 0:
            rating = int(rating) + 1
            if rating == 101:
                break
            list_of_games = rating_map.retrieve(rating)
            while len(list_of_games) > remaining:
                list_of_games.pop()
            current_list = len(list_of_games)
            remaining = remaining - current_list
            
            if list_of_games != []:
                for i in range(current_list):
                    print(f'''
        Name: {list_of_games[0][0]}
Release date: {list_of_games[0][1]}
      Rating: {list_of_games[0][2]}
      Genres: {list_of_games[0][3]}
   Platforms: {list_of_games[0][4]}
''')
                    list_of_games.pop(0)
    
        self.cont()
            



system('cls' if osname == 'nt' else 'clear')
main = Main()