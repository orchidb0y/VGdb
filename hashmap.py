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
        print('\nNow inside HashMap object')
        print(f'Assigning/retrieving the game {key} to {self}')
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + coll_count

    def compressor(self, hash_code):
        return hash_code % self.size

    def assign(self, key, value):
        index = self.compressor(self.hash(key))
        print(f'Assigning game to index {index}')
        current_array_value = self.array[index]
        if current_array_value == None:
            self.array[index] = [key, value]
            print('Assignment complete')
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