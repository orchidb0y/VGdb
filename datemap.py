from hashmap import *
from datetime import date

class DateMap:

    def __init__(self):
        self.array = [HashMap(50) for month in range(516)]

    def get_index(self, release_date):
        date_list = str(release_date).split('-')
        year = int(date_list[0])
        month = int(date_list[1])

        return ((year - 1980) * 12) + (month - 1)

    def assign(self, release_date, values):
        index = self.get_index(release_date)
        print(f'\nAssigning game to index {index}')
        current_array_hashmap = self.array[index]
        print('Assigning to hashmap', current_array_hashmap, 'at index', self.array.index(current_array_hashmap))
        print(f'Key to be used is {values[0]} and value is {values}')
        current_array_hashmap.assign(values[0], values)

    def retrieve(self, release_date):
        index = self.get_index(release_date)
        print(f'\nRetrieving hashmap from index {index} onwards')
        return_hashmap = self.array[index]

        list_of_games = []

        remaining = 10
        while index <= 515 and remaining >= 0:
            for game in self.array[index]:
                # print(f'Getting games from index {index}')
                if game != None:
                    list_of_games.append(game[1])
                    remaining -= 1
            index += 1
            print(f'Index at {index} and {remaining} games remaining')
        
        return list_of_games


# game = {'Name': 'Cool game', 'Rating': 95, 'Release date': date(2004, 6, 12)}
# datemap = DateMap()

# datemap.assign(game['Release date'], list(game.values()))
# print(datemap.retrieve(date(2004, 6, 12)))