# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 04:41:51 2018

@author: Natthinee
"""
import pymongo
from pymongo import MongoClient


def scoreC():
    client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
    db  = client.khim.user
    count = 0
    for i in db.find():
        if i['Question'] == '1':
            score = i['Question']
            count = int(score)
    return count
        
