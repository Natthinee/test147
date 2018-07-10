# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 04:41:51 2018

@author: Natthinee
"""
import pymongo
from pymongo import MongoClient
number = ['0','1','2','3']

def scoreC(userid,question):
    client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
    db  = client.khim.user
    count = 0
    score = 0
    for i in db.find():
        if(userid == i['UserID']):
            if i['Question'] in number:
                score = i['Question']
                count = int(score) + count
    print(count)
    return str(count)

def countQues(userid,question):
    client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
    db  = client.khim.user
    count = 0
    score = 0
    for i in db.find():
        if(userid == i['UserID']):
            if i['Question'] in number:
                count = count+1
    print(count)            
    return str(count)
        
