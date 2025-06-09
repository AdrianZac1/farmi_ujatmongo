from pymongo import MongoClient

def get_database():
    
    uri = "mongodb+srv://221h17005:z2ujnai0BXUHF2ej@farmiujat.spybiqw.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri)
    return client["farmacia_ujat"]

def get_collections():
    
    db = get_database()
    return db["farmaco"], db["medicamento"]

