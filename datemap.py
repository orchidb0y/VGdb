from hashmap import *
from linkedlist import *
from datetime import date
from random import shuffle

class DateMap:

    def __init__(self):
        self.array = [LinkedList() for year in range(44)]

    def get_index(self, release_date):
        date_list = str(release_date).split('-')
        year = int(date_list[0])

        return year - 1979

    def assign(self, release_date, values):
        index = self.get_index(release_date)
        print(f'\nIndex to be used is {index}')
        print(f'Assigning game to index {index}')
        current_array_linkedlist = self.array[index]
        print('Assigning to LinkedList', current_array_linkedlist, 'at index', self.array.index(current_array_linkedlist))
        print(f'Value to be used is {values}')
        current_array_linkedlist.insert_beginning(values)

    def retrieve(self, release_date):
        index = self.get_index(release_date)
        print(f'\nRetrieving LinkedList from index {index} onwards')

        list_of_games = []
        current_node = self.array[index].get_head_node()

        while current_node.get_value() != None:
            list_of_games.append(current_node.get_value())
            current_node = current_node.get_next_node()
        
        return list_of_games