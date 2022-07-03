# This is a regular hashmap class, and is used by the program to store the games and
# search by name using the list provided by findname.py.

class HashMap:

    def __init__(self, size):
        self.size = size
        self.array = [None for item in range(size)]
        self.empty = True

    def __iter__(self):
        self.n = 0
        return self 

    def __next__(self):
        if self.n <= self.size:
            result = self.array[self.n - 1]
            self.n += 1
            return result
        else:
            raise StopIteration

    def hash(self, key, coll_count = 0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + coll_count

    def compressor(self, hash_code):
        return hash_code % self.size

    def assign(self, key, value):
        index = self.compressor(self.hash(key))
        current_array_value = self.array[index]
        if current_array_value == None:
            self.array[index] = [key, value]
            self.empty == False
            return

        coll_count = 1
        while current_array_value[0] != key:
            new_index = self.compressor(self.hash(key, coll_count))
            current_array_value = self.array[new_index]
            if current_array_value == None:
                self.array[new_index] = [key, value]
                self.empty == False
                return
            coll_count += 1
    
    def retrieve(self, key):
        index = self.compressor(self.hash(key))
        possible_value = self.array[index]

        if possible_value[0] == key:
            return possible_value[1]
        
        coll_count = 1
        while possible_value[0] != key:
            new_index = self.compressor(self.hash(key, coll_count))
            possible_value = self.array[new_index]
            if possible_value[0] == key:
                return possible_value[1]
            coll_count += 1