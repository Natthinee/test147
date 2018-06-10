import pymongo
from pymongo import MongoClient
import json
tt = []

def find1(question,answer):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.user
   #w = db.user.find_one()
   #w = db.find({'Question': 'แบบประเมิน' }).sort(answer)
   for item in db.user.find():
   return item
