from hashmap import *

class RatingMap:

    def __init__(self):
        self.array = [HashMap(20) for item in range(101)]

    def assign(self, key, value):
        index = int(key)
        print(f'\nAssigning game to index {index}')
        current_array_hashmap = self.array[index]
        print('Assigning to hashmap', current_array_hashmap, 'at index', self.array.index(current_array_hashmap))
        print(f'Key to be used is {value[0]} and value is {value}')
        current_array_hashmap.assign(value[0], value)

    def retrieve(self, key):
        index = int(key)
        print(f'\nRetrieving hashmap from index {index}')
        return_hashmap = self.array[index]
        print(f'Retrieving from hashmap', return_hashmap, 'at index', index)

        list_of_games = []

        for game in return_hashmap:
            if game != None:
                list_of_games.append(game[1])
        
        return list_of_games