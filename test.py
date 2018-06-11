import pymongo
from pymongo import MongoClient
import json
quest9 = open("Quest9.txt", "r", encoding='utf-8-sig')
quest9 = quest9.read().split(',')
tt = []
score = 0
def find1(face,question1):
     client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
     db  = client.khim.user
     for i in db.find():
          if question1 != i['Answer']:
                return face + question1
          else:
                return 'ทดสอบใหม่'

  
