import pymongo
from pymongo import MongoClient
import json
tt = []

def find1():
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.user
   g = db.insert({'สวัสดี':'ขิมเองจ้า'})
   w = db.find({'Question':  "Dbfusv"}).sort("Answer")
   data = w.json()
   j = json.loads(data)
   return j['Question']
