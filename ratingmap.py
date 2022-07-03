from hashmap import *
from linkedlist import *

# This class is used to store games from the main database based on rating.
# There is a linkedlist for each rating, and games with the same rating are stored in these linkedlists.

class RatingMap:

    def __init__(self):
        self.array = [LinkedList() for rating in range(101)]

    def assign(self, rating, value):
        index = int(rating)
        current_array_linkedlist = self.array[index]
        current_array_linkedlist.insert_beginning(value)

    def retrieve(self, rating):
        index = int(rating)
        return_hashmap = self.array[index]

        list_of_games = []
        current_node = self.array[index].get_head_node()

        while current_node.get_value() != None:
            list_of_games.append(current_node.get_value())
            current_node = current_node.get_next_node()
        
        return list_of_games