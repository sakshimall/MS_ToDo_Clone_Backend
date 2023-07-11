import pickle
from os.path import exists

file_name = "saved.pkl"
value = {"My Day": {"title":"My Day", "pending":[], "completed":[]}}

def getDataFromMongo():
    if exists(file_name):
        with open(file_name, 'rb') as file:
            return pickle.load(file)    
    return value

def postDataFromMongo(data: dict):
    if len(list(data.keys())):
        with open(file_name, 'wb') as file:
            pickle.dump(data, file)
