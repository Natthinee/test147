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
mid = open("mid.txt", "r", encoding='utf-8-sig')
mid = mid.read().split(',')
wordappende = open("wordappende.txt", "r", encoding='utf-8-sig')
wordappende = wordappende.read().split(',')
qq2 = open("qq2.txt", "r", encoding='utf-8-sig')
qq2 = qq2.read().split(',')
t9 = open("TT.txt", "r", encoding='utf-8-sig')
t9 = t9.read().split('\n')
excusive = open("Excusive.txt", "r", encoding='utf-8-sig')
excusive = excusive.read().split(',')
exq8 = open("Exq8.txt","r", encoding='utf-8-sig')
exq8 = exq8.read().split(',')
ans8 = {}
idsub =[]
q2sub = []
q8sub = []
q8subx = []
q8suby = []
q8subxy = []
number = ['0','1','2','3']
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
ple = 'ช่วยพิมพ์คำตอบว่า "มี" ถ้าเกิดมีอาการที่สอดคล้องกับคำถาม\nพิมพ์คำว่า "ไม่มี" ถ้าเกิดไม่มีอาการที่สอดคล้องกับคำถามหน่อยนะจ๊ะ (◕‿◕✿)'
ple8 = 'ตอบว่า "ใช่" หากเคยมีเหตุการณ์ังกล่า'
game = 'พักสมองสักเเปบดีกว่าน้าา\nก่อนอุ่นมีเกมส์มาให้ทาย สนใจไหม\n ถ้าสนใจก็พิมพ์คำว่า "สนใจ"\nเเต่ถ้าอยากทำต่อ ก็พิมพ์คำว่า "ไปต่อ" นะจ๊ะ'
#client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
#db  = client.khim.user
#for i in db.find():
    #print(i['UserID'])
    #idsub.append(i['UserID'])
   
def find1(userid,question):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.user
   numb = ['0','1','2','3']
   count1 = 0 
   count2 = 0
   No = 0
   No1 = 0
   round = 1
   for i in db.find():
        if(userid==i['UserID']):
            if i['Question'] in numb:
                  count1 = count1+1
                  No =  No+1
                  print(count1)
                  print(No)
            if i['Question'] == "ทำต่อจากเดิม":
                  count1 = count1-1
                  No =  No-1
                  print(count1)
   for i in db.find():
        #print(i['UserID'])
        idsub.append(i['UserID'])
   if userid not in idsub:
        count2 = count1
        answer = t9[count2]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer
   if userid in idsub:
        count2 = count1
        answer = t9[count2]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer

def findxx(userid,question):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.user
   count1 = 0 
   No = 0
   for i in db.find():
        if(userid==i['UserID']):
            No = No + 1
   print(No)
   return No  
  
def findyy(userid,question):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.Q2
   count1 = 0 
   No = 0
   for i in db.find():
        if(userid==i['UserID']):
            No = No + 1
   print(No)
   return No  
        
def find2(userid,question):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.Q2
   count1 = 0 
   count2 = 0
   No = 0
   No1 = 0
   round = 2
   for i in db.find():
        if(userid==i['UserID']):
            count1 = count1+1
   for i in db.find():
        if(userid==i['UserID']):
            No = No + 1       
   for i in db.find():
        print(i['UserID'])
        q2sub.append(i['UserID'])
   if userid not in q2sub:
        count2 = count1
        answer = qq2[count1]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer
   if userid in q2sub:
        count2 = count1
        answer = qq2[count1]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer  
      
def find3(userid,question):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.Q8
   count1 = 0 
   count2 = 0
   No = 0
   No1 = 0
   round = 3
   for i in db.find():
        if(userid==i['UserID']):
            count1 = count1+1
   for i in db.find():
        if(userid==i['UserID']):
            No = No + 1       
   for i in db.find():
        print(i['UserID'])
        q8sub.append(i['UserID'])
   if userid not in q8sub:
        count2 = count1
        answer = quest8[count2]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer
   if userid in q8sub:
        count2 = count1
        answer = quest8[count2]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer 
      
def findx(userid,question):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.QQ8
   count1 = 0 
   count2 = 0
   No = 0
   No1 = 0
   round = 4
   for i in db.find():
        if(userid==i['UserID']):
            No = No + 1       
   for i in db.find():
        print(i['UserID'])
        q8subx.append(i['UserID'])
   for i in db.find():
        if(userid==i['UserID']):
            count1 = count1+1
   if userid not in q8subx:
        count2 = count1
        answer = excusive[count2]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer
   if userid in q8subx:
        count2 = count1
        answer = excusive[count2]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer 

def findy(userid,question):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.QQQ8
   count1 = 0 
   count2 = 0
   No = 0
   No1 = 0
   round = 5
   for i in db.find():
        if(userid==i['UserID']):
            No = No + 1       
   for i in db.find():
        print(i['UserID'])
        q8suby.append(i['UserID'])
   for i in db.find():
        if(userid==i['UserID']):
            count1 = count1+1
   if userid not in q8suby:
        count2 = count1
        answer = exq8[count2]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer
   if userid in q8suby:
        count2 = count1
        answer = exq8[count2]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer 

      
def findxy(userid,question):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.QQQQ8
   count1 = 0 
   count2 = 0
   No = 0
   No1 = 0
   round = 6
   for i in db.find():
        if(userid==i['UserID']):
            No = No + 1       
   for i in db.find():
        print(i['UserID'])
        q8subxy.append(i['UserID'])
   for i in db.find():
        if(userid==i['UserID']):
            count1 = count1+1
   if userid not in q8subxy:
        count2 = count1
        answer = mid[count2]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer
   if userid in q8subxy:
        count2 = count1
        answer = mid[count2]
        No1 = No
        db.insert({"UserID":userid,"Round":round,"No":No1,"Question": question, "Answer": answer})
        return answer 
      
def deleteQu(userid,question):
   client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
   db  = client.khim.user
   dd  = client.khim.Q2
   db.delete_many({'UserID':userid})
   dd.delete_many({'UserID':userid})
   return 'มาทำเเบบประเมินกันเถอะ'

                
                
   
   
   
  
#def continues2(userid,question):
      
            
                      
             
              
        
            
            
   


        
        
   

        
      
      
    


    
          

        
     

  
