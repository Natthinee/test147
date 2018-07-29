# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 09:17:34 2018

@author: Natthinee
"""

import pymongo
from pymongo import MongoClient
import decimal 
d = decimal.Decimal 

client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
db  = client.khim.province_Hospital
dd  = client.khim.hospital_address 
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

def addressPro(question):
    for i in dd.find():
        if(i['province']== question ):
             address = i['address']
             web = i['website']
             telophone = i['tel']
            
    return 'ที่อยู่โรงพยาบาล:\n'+address+'\n'+'เว็บไซต์โรงพยาบาล:\n'+web+'\n'+'เบอร์โทรศัพท์:\n'+ telophone

def namehosLati(question):
    for i in db.find():
        if(i['hospital'] == question):
            return float(i['Latitude']
                         
def namehoslong(question):
    for i in db.find():
        if(i['hospital'] == question):
            return float(i['longitude'])
                         
                         
def provinceehos(question):
    for i in db.find():
        if(i['hospital']== question ):
            return i['province']
                         
def addressProhos(question):
    for i in dd.find():
        if(i['hospital']== question ):
             address = i['address']
             web = i['website']
             telophone = i['tel']
            
    return 'ที่อยู่โรงพยาบาล:\n'+address+'\n'+'เว็บไซต์โรงพยาบาล:\n'+web+'\n'+'เบอร์โทรศัพท์:\n'+ telophone
                         
                         
def hospiName(question):
    for i in db.find():
        if(i['hospital']== question ):
            return i['hospital']
                         
                         

                         
    
    
    

    
    
    
    
            
   
