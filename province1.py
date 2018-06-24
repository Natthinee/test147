# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 09:17:34 2018

@author: Natthinee
"""

import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
db  = client.khim.province_Hospital
def Latitudee(question):
    for i in db.find():
        if(i['province'] == question):
            return float(i['Latitude'])
                
def longtitutee(question):
    for i in db.find():
        if(i['province'] == question):
            return float(i['longitude'])
        
def hospitalName(question):
    for i in db.find():
        if(i['province']== question ):
            return i['hospital']
        
def provincee(question):
    for i in db.find():
        if(i['province']== question ):
            return i['province']
    
    
    
            
   
