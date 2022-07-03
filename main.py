from os import system
from os import name as osname
from hashmap import *
from games import *
from findname import *
from ratingmap import *
from datemap import *
from linkedlist import *

class Main:

    def __init__(self):
        self.start()

    def get_option(self):
        print('''
1) Search by name
2) Search by rating
3) Search by release date
4) Search by genre
5) Search by platform''')

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
            if opt == '3':
                self.by_release()
            if opt == '4':
                self.by_genre()
            if opt == '5':
                self.by_platform()
        
        else:
            print('\nThank you for using VGdb!')

    def start(self):
        opt = self.get_option()

        if opt == '1':
            self.by_name()
        if opt == '2':
            self.by_rating()
        if opt == '3':
            self.by_release()
        if opt == '4':
            self.by_genre()
        if opt == '5':
            self.by_platform()
        if opt not in ['1', '2', '3', '4', '5']:
            print('You entered an invalid choice. Try again.')
            self.start()
    
    def by_name(self):
        name_map = HashMap(500)

        for game in games:
            name_map.assign(game['Name'], list(game.values()))

        name = input('\nEnter a part of the name of the game you are looking for (min 3 characters): ')
        while len(name) < 3:
            name = input('Please enter a minimum of three characters: ')

        name_list = [game['Name'] for game in games]
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
        
        for game in games:
            rating_map.assign(game['Rating'], list(game.values()))
        
        rating = input('''\nThe program will return a list of 10 games that have equal or higher metacritic score.
Pick a rating from 1-100: ''')
        while int(rating) > 100 or int(rating) < 1:
            rating = input('Please enter a number between 1-100: ')

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
            
    def by_release(self):
        datemap = DateMap()

        for game in games:
            datemap.assign(game['Release date'], list(game.values()))

        date_search = input('''\nThe program will return 10 games released on the release date or later.
Enter a date in the YYYY-MM-DD format (e.g. 1994-11-25): ''')

        while True:
                try:
                    date_parts = date_search.split('-')

                    while 1980 > int(date_parts[0]) or int(date_parts[0]) > 2022:
                        date_search = input('''\nThe date you entered is not valid. Only dates between 1980 and 2022 (included) are valid.
Remember to enter a date in the YYYY-MM-DD format: ''')

                    date_search = date(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
                    break
                except ValueError:
                    date_search = input('''\nSome value you entered is incorrect.
Remember to enter a date in the YYYY-MM-DD format: ''')


        list_of_games = datemap.retrieve(date_search)

        for game in list_of_games:
            print(f'''
        Name: {game[0]}
Release date: {game[1]}
      Rating: {game[2]}
      Genres: {game[3]}
   Platforms: {game[4]}
''')

        self.cont()

    def by_genre(self):
        genre_list = {}

        for genre in genres:
            genre_list[genre] = LinkedList()

        for game in games:
            for genre in game['Genres']:
                genre_list[genre].insert_beginning(game)
        
        pick = input(f'\nChoose a genre from this list: {genres}. Enter your choice: ').title()

        while True:
            if pick in genres:
                break
            else:
                pick = input(f'''\nYou picked an invalid genre. Please enter a genre in this list: {genres}.
Enter your choice: ''').title()
        
        print('\nThe game will return 10 games that match the genre you picked.')
        remaining = 10
        list_of_games = []

        current_node = genre_list[pick].get_head_node()
        list_of_games.append(current_node.value)
        remaining -= 1

        while remaining > 0:
            current_node = current_node.get_next_node()
            if current_node.value != None:
                list_of_games.append(current_node.value)
                remaining -= 1
            else:
                break

        for game in list_of_games:
            print(f'''
        Name: {game['Name']}
Release date: {game['Release date']}
      Rating: {game['Rating']}
      Genres: {game['Genres']}
   Platforms: {game['Platforms']}
''')

        self.cont()

    def by_platform(self):
        platform_list = {}

        for platform in platforms:
            platform_list[platform] = LinkedList()
        
        for game in games:
            for platform in game['Platforms']:
                platform_list[platform].insert_beginning(game)
        
        pick = input(f'\nChoose a platform from this list: {platforms}. Enter your choice: ').title()

        while True:
            if pick in platforms:
                break
            else:
                pick = input(f'''\nYou picked an invalid platform. Please enter a platform in this list: {platforms}.
Enter your choice: ''').title()

        print('\nThe game will return 10 games that match the platform you picked.')
        remaining = 10
        list_of_games = []

        current_node = platform_list[pick].get_head_node()
        list_of_games.append(current_node.value)
        remaining -= 1

        while remaining > 0:
            current_node = current_node.get_next_node()
            if current_node.value != None:
                list_of_games.append(current_node.value)
                remaining -= 1
            else:
                break
        
        for game in list_of_games:
            print(f'''
        Name: {game['Name']}
Release date: {game['Release date']}
      Rating: {game['Rating']}
      Genres: {game['Genres']}
   Platforms: {game['Platforms']}
''')

        self.cont()



system('cls' if osname == 'nt' else 'clear')
print('Welcome to the VGdb v1.0b')
main = Main()