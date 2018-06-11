import pymongo
from pymongo import MongoClient
import json
number = ['0', '1', '2', '3']
quest9 = open("Quest9.txt", "r", encoding='utf-8-sig')
quest9 = quest9.read().split(',')
tt = []
score = 0
def find1():
     client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
     db  = client.khim.user
     for i in db.find():
          if i['Answer'] in quest9:
               score = score + 1
     return score

  
