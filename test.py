import pymongo
from pymongo import MongoClient
import json
tt = []

def find1(question,answer):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.user
   w = db.find({'Question': question }).sort(answer)
   for i in w:
      tt.append(i)
   return tt
