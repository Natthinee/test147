
'''
from pymongo import MongoClient


client = MongoClient("mongodb://pretty:shop1234@ds139942.mlab.com:39942/moviebot")
db = client.moviebot

def findmovie():
        cursor = db.users.find()  #หาuser id

        for i in cursor:
            print(i)

findmovie()

'''

