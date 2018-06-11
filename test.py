import pymongo
from pymongo import MongoClient
import json
tt = []
def find1():
     client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
     db  = client.khim.user
     for i in db.find():
          if i["Question"] ==
     return tt

  
