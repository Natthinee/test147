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
qq2 = open("qq2.txt", "r", encoding='utf-8-sig')
qq2 = qq2.read().split(',')
quest8 = open("QQ8.txt", "r", encoding='utf-8-sig')
quest8 = quest8.read().split(',')


tt = []
score = 0
#q9Ran = random.choice(QC)
def find1():
     client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
     db  = client.khim.user
     countData = db.count()
     if countData <= 9:
          return QC1[countData-1]
def find2():
     if countData <= 11:
          return qq2[countData-10]
     elif countData <= 20:
          return quest8[countData-12]
     else:
          return 'ถ้าอยากทราบผลการประเมินเลยให้พิมพ์คำว่า "ผลลัพธ์"\nแต่ถ้าอยากลองฟังก์ชันการใช้งานอื่นดูก่อนก็สามารถกดได้ที่ปุ่มฟังก์ชันต่างๆ\nที่หน้าจอได้เลยน้าา ◑０◐'
          
          
          

          
          
          
          
          
          
          
     

  
