import pymongo
from pymongo import MongoClient
tt = []
def find1():
     client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
     db  = client.khim.user
     g = db.insert({'สวัสดี':'12','จ้า':'n'})
#g2 = db.user.insert({'สวัสดี':'21'})
#db.users.remove({z:'abc'});
     for i in db.find():
         tt.append(i['จ้า'])
      return tt

  
