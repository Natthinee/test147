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
            return float(i['Latitude'])
                         
def namehosLong(question):
    for i in db.find():
        if(i['hospital'] == question):
            return float(i['longitude'])
                         
                         
def provinceehos(question):
    for i in db.find():
        if(i['hospital'] == question):
            return i['province']
                         
def addressProhos(question):
    for i in dd.find():
        if(i['hospital'] == question):
             address = i['address']
             web = i['website']
             telophone = i['tel']
            
    return 'ที่อยู่โรงพยาบาล:\n'+address+'\n'+'เว็บไซต์โรงพยาบาล:\n'+web+'\n'+'เบอร์โทรศัพท์:\n'+ telophone
                         
                         
def hospiName(question):
    for i in db.find():
        if(i['hospital']== question ):
            return i['hospital']
        
def prohospital2(question):
    hospro = []
    for i in db.find():
        if(i['province']== question):
            hospro.append(i['hospital'])
    return hospro

def hospro1(question):
    kublisthos = prohospital2(question)
    return kublisthos[0]

def hospro2(question):
    kublisthos = prohospital2(question)
    return kublisthos[1]

def tud2prov(question):
    nametud = []
    for i in db.find():
        if i['province']==question:
             test1 = i['hospital'].split("โรงพยาบาล")
             test = test1[1].split("(")
             test2 = test[0]
             nametud.append(test2)
              #print(test1)
              #print(test)
              #print(test2)
    return nametud

def tud21(question):
    tu = tud2prov(question)
    return tu[0]
    
def tud22(question):
    tu = tud2prov(question)
    return tu[0]
    
            
    

    
            
                         
                         

                         
    
    
    

    
    
    
    
            
   
