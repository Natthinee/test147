import pymongo
from pymongo import MongoClient
import json
import random
QC1 = open("QC1.txt", encoding='utf-8-sig')
QC1 = QC1.read().split(',')
QC2 = open("QC1.txt", encoding='utf-8-sig')
QC2 = QC2.read().split(',')
QC3 = open("QC1.txt", encoding='utf-8-sig')
QC3 = QC3.read().split(',')
QC4 = open("QC1.txt", encoding='utf-8-sig')
QC4 = QC4.read().split(',')
QC5 = open("QC1.txt", encoding='utf-8-sig')
QC5 = QC5.read().split(',')
QC6 = open("QC1.txt", encoding='utf-8-sig')
QC6 = QC6.read().split(',')
QC7 = open("QC1.txt", encoding='utf-8-sig')
QC7 = QC7.read().split(',')
QC8 = open("QC1.txt", encoding='utf-8-sig')
QC8 = QC8.read().split(',')
QC9 = open("QC1.txt", encoding='utf-8-sig')
QC9 = QC9.read().split(',')
QC =[QC1,QC2,QC3,QC4,QC5,QC6,QC7,QC8,QC9]

tt = []
score = 0
def find1(question):
     client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
     db  = client.khim.user
     for i in db.find():
          if i['Answer'] == None:
               return face + question1
          if question1 != i['Answer']:
               return face + question1
          if len(i['Answer']) == 9:
               return 'ทดสอบใหม่'
          
 def ran():
      QC = random.choice(QC)
      return QC[1]
          
          
          
          
          
          
          
          
     

  
