# Nathan Chuluda
# CS-340-T3703 Client/Server Development 22EW3
# Module 4 Milestone
# January 27, 2022

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:53570' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if self.database.animals.insert_one(data):  # data should be dictionary            
            print("record added")
        else:
            raise Exception("Error adding record.")

# Create method to implement the R in CRUD. 
    def read(self, search):
        return self.database.animals.find(search, {"_id":False})
    

# Create method to implement the U in CRUD.
    def update(self, search, data):
        return self.database.animals.update(search, data)

# Create method to implement the D in CRUD.
    def delete(self, search):
        return self.database.animals.remove(search)