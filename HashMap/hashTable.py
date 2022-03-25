
class HashTable:
    def __init__(self):
        self.myHash = {}



    def insert_data(self, key, data):

        if key in self.myHash:
            print("Key already exists")
        else:
            self.myHash[key] = data

    def delete_data(self, key):

        if key in  self.myHash:
            del  self.myHash[key]
        else:
            print("Key dont exist")
        
    def update_data(self, key, data):

        if key in self.myHash:
            self.myHash[key] = data
        else:
            print("Key dont exist")

    def search_data(self, key):

        if key in self.myHash:
            print( self.myHash[key])
        else:
            print("Key dont exist")
        


map = HashTable()

map.insert_data("0x0c09283490nsjdhfiusdhfiu02u89whed", 10)

map.search_data("0x0c09283490nsjdhfiusdhfiu02u89whed")
