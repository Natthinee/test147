import pymongo
from pymongo import MongoClient
import json
tt = []

def find1(question,answer):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.user
   #data = db.user.find()
   ttt = posts.find({"_id": {"$oid": "5b1cd22a2a76fe1393ef95f5"}}).sort("Question")
   for post in ttt:
      tt.append(post)
   return tt

  
