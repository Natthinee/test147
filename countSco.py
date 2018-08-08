# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 04:41:51 2018

@author: Natthinee
"""
import pymongo
from pymongo import MongoClient
number = ['0','1','2','3']
me = ['มี','ไม่มี','มี.','ไม่มี.']
me1 = ['มี','มี.']
me2 = ['ไม่มี.','ไม่มี']
filephoto = open("ไฟล์รูป.txt", "r", encoding='utf-8-sig')
filephoto = filephoto.read().split('\n')

def scoreC(userid,question):
    client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
    db  = client.khim.user
    count = 0
    score = 0
    total = 0
    for i in db.find():
        if(userid == i['UserID']):
            if i['Question'] in number:
                score = i['Question']
                count = int(score) + count
    if(count < 7):
        answer = '◎◎◎ ประเมินจากเเบบประเมิน 9Q\n◈◈◈ ผลการประเมิน\n►ไม่มีอาการของโรคซึมเศร้าหรือ\nมีอาการของโรคซึมเศร้าระดับน้อยมาก\nเอ๊ะ!อยากลองใช้ฟังก์ชันเพิ่มเติมไหมนะ\nถ้าอยากลองพิมพ์ "ฟังก็ชันเพิ่มเติม"' 
    elif(count >= 7 and count <= 12):
        answer = '◎◎◎ ประเมินจากเเบบประเมิน 9Q\n◈◈◈ ผลการประเมิน\n►มีอาการของโรคซึมเศร้า"ระดับน้อย"\nเอ๊ะ!อยากลองใช้ฟังก์ชันเพิ่มเติมไหมนะ\nถ้าอยากลองพิมพ์ "ฟังก็ชันเพิ่มเติม"' 
    elif(count >= 13 and count <=18):
        answer = '◎◎◎ ประเมินจากเเบบประเมิน 9Q\n◈◈◈ ผลการประเมิน\n►มีอาการของโรคซึมเศร้า"ระดับปานกลาง"โห่วอาการเริ่มน่าเป็นห่วง\nไปหาจิตเเพทย์ใกล้บ้านกันเถอะ\nพิมพ์คำว่า "จิตเวชใกล้บ้าน"หรือลอง\nกดโทร 1323 คุยกับสายด่วนสุขภาพจิต\nก่อนก็ได้นะ'
    elif(count >= 19):
        answer = '◎◎◎ ประเมินจากเเบบประเมิน 9Q\n◈◈◈ ผลการประเมิน\n►มีอาการของโรคซึมเศร้า"ระดับรุนแรง"โห่วอาการน่าเป็นห่วงมาก!!\nควรไปพบจิตเเพทย์ใกล้บ้านโดยด่วน!!\nพิมพ์คำว่า "จิตเวชใกล้บ้าน"' 
    total = (count*100)/27    
    print(count)
    return answer
def scoreQ2(userid,question):
    client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
    db  = client.khim.Q2
    count = 0
    for i in db.find():
        if(userid == i['UserID']):
            if i['Question'] in me1:
                count = count + 1
    print(count)
    if(count>=1):
        answer  = '★★★ประเมินโอกาสเสี่ยงจากเเบบประเมิน 2Q \n▩▩ ผลการประเมิน\n►มีโอกาสเสียงที่จะเป็นโรคซึมเศร้า'
    else:
        answer  = '★★★ประเมินโอกาสเสี่ยงจากเเบบประเมิน 2Q \n✖✖ ผลการประเมิน\n►ไม่มีโอกาสเสียงที่จะเป็นโรคซึมเศร้า'     
    return answer

def scorephoto(userid,question):
    client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
    db  = client.khim.user
    count = 0
    score = 0
    total = 0
    for i in db.find():
        if(userid == i['UserID']):
            if i['Question'] in number:
                score = i['Question']
                count = int(score) + count
    return filephoto[count]

def scoreme2(userid,question):
    client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
    db  = client.khim.Q2
    count = 0
    for i in db.find():
        if(userid == i['UserID']):
            if i['Question'] in me2:
                count = count + 1
    if(count == 2):
        return "ปกติจ้า"
    else:
        return "ไม่ปกติ"
    

































    

        
