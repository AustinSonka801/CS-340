from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient to access the database
        USER = 'accuser'
        PASS = 'austin1'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31099
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert_result = self.collection.insert_one(data)  # data should be a dictionary
            if insert_result.inserted_id:
                status = True
            else:
                status = False
            return status
        else:
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            animalsCollection = self.collection.find(data)
            for animals in animalsCollection:
                print(animals)
        else:
            raise Exception("No search criteria provided")

    # Create u in crud
    def update(self, query, record):
        if record is not None:
            update_result = self.collection.update_many(query, record)
            result = "Documents updated: " + json.dumps(update_result.modified_count)
            return result
        else:
            raise Exception("Nothing to update, because data parameter is empty")

    # D in crud
    def delete(self, data):
        if data is not None:
            delete_result = self.collection.delete_many(data)
            result = "Documents deleted: " + json.dumps(delete_result.deleted_count)
            return result
