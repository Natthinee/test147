import pymongo
from pymongo import MongoClient
import json
tt = []
client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
db  = client.khim.user
def find1():
   for i in db.find():
      tt.append(i['Answer'])
   return tt

  
