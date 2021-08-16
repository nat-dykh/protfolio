from pymongo import MongoClient
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username = None, password = None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:54690/AAC' % (username, password))
        self.database = self.client['AAC']

# Method for creating
    def create(self, data):
        if (data != None):
            insert = self.database.animals.insert(data)
            if (insert != None):
                return "true"
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            

# Method for reading 
    def read(self, query): 
        if (query != None):
            x = self.database.animals.find(query)
            return(x)
        else:
            x = self.database.animals.find()
            return(x)
  
# Method for updating
    def update(self,old, new):
        if (old != None and new != None):
            x =self.database.animals.update(old,new)
            return (x)
        else:
            return Exception("Nothing to save, because data parameter is empty")
                                  
#Method for deleting data
    def delete(self,data):
        if (data!= None):
            x = self.database.animals.deleteOne(data)
            return(x)
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            
                                  
            