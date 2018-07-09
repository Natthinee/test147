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
sayhi = open("sayhi.txt", encoding='utf-8-sig')
sayhi = sayhi.read().split(',')
answer = open("answer.txt", "r", encoding='utf-8-sig')
answer = answer.read().split(',')
ques = open("Ques.txt", "r", encoding='utf-8-sig')
ques = ques.read().split(',')
wordappende = open("wordappende.txt", "r", encoding='utf-8-sig')
wordappende = wordappende.read().split(',')
qq2 = open("qq2.txt", "r", encoding='utf-8-sig')
qq2 = qq2.read().split(',')
t9 = open("TT.txt", "r", encoding='utf-8-sig')
t9 = t9.read().split('\n')
ans8 = {}
count1 = 0 ####### count1 คือนับรอบการทำ
count2 = 0
No = 0
ans8['ans'] = {'an': 'ไม่ได้',
               'ay': 'ได้'}
please = {}
please['ple'] = {'ple': 'กรุณาพิมพ์หมายเลข 0 1 2 3 ตามระดับของอาการที่เป็นหน่อยน้าาา',
                 'ple1': 'พิมพ์ "มี" หน่อยนะถ้ามีอาการ พิมพ์ "ไม่มี" ถ้าไม่มีอาการน้าาา',
                 'ple2': 'กรุณาตอบ "ไม่มี" ถ้าไม่มีอาการ หรือตอบ "มี" ถ้าไม่มีอาการ',
                 'ple3': 'กรุณาตอบ "ได้" หากสามารถควบคุมอารมณ์ตัวเองได้ ตอบ "ไม่ไ้ด้" หากท่านไม่สามารถควบคุมอารมณ์ตนเองได้',
                 'Error': '-- เอ๊ะ! พิมพ์ผิดหรือเปล่าน้าาาา กอดอุ่นไม่เห็นเข้าใจเลย :/'}
answer0123 = {}
answer0123['answer0123'] = {'answer0': 'ไม่มีเลย',
                            'answer1': 'เป็นบางวัน',
                            'answer2': 'เป็นบ่อย',
                            'answer3': 'เป็นทุกวัน'}
setscoreq9 = {}
setscoreq9['score'] = {'pprint': ' 0 = ไม่มีเลย\n 1 = เป็นบางวัน\n 2 = เป็นบ่อย\n 3 = เป็นทุกวัน\n'}
select2 = {}
select2['selc'] = {'selc01': 'มี',
                   'selc02': 'ไม่มี'}
evaluation_form = {}
evaluation_form['eval'] = {'greet': sayhi,
                           'answer': answer,
                           'ques': ques,
                           'wordap': wordappende,
                           'qq2': qq2}
sayYN = {}
sayYN['yn'] = {'yes':'ใช่','no':'ไม่ใช่'}
sayPatt = 'นี่ๆ ช่วยพิมพ์ ว่า "ใช่" ถ้าเกิดว่ามีลักษณะอาการที่ตรงกับสิ่งที่กอดอุ่นถาม เเต่ถ้าไม่มีลักษณะอาการตามที่ถามก็พิมพ์ว่า "ไม่ใช่" หน่อยน้า\n'
score = 0
arr = 0
number = ['0','1','2','3']
ple = 'ช่วยพิมพ์คำตอบว่า "มี" ถ้าเกิดมีอาการที่สอดคล้องกับคำถาม\nพิมพ์คำว่า "ไม่มี" ถ้าเกิดไม่มีอาการที่สอดคล้องกับคำถามหน่อยนะจ๊ะ (◕‿◕✿)'
ple8 = 'ตอบว่า "ใช่" หากเคยมีเหตุการณ์ังกล่า'
def find1(userid,question):
    client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
    db  = client.khim.user
    countData = db.count()
    if countData == 0:
       count1 = 1
       arr = 1
       answer = t9[0]
    db.insert({"UserID":userid,"Round":count1,"No":arr,"Question": question, "Answer": answer})
    else:
       for i in db.find():
            if userid == i['UserID']:
                  count1 = 1
                  arr = 1
                  answer = t9[1]
    db.insert({"UserID":userid,"Round":count1,"No":arr,"Question": question, "Answer": answer}) 
    return answer
def find2(userid,question):
    #db.insert({"UserID":userid,"Round":count1,"No":No,"Question": question, "Answer": answer})
    return 'kkkk'
def find3(userid,question):
    return 'llllll'

    
          

        
     

  
