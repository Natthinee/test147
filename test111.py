# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:41:11 2018

@author: Natthinee
"""

import re 
evaluation_form = {}
number = ['0', '1', '2', '3']
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
province = open("province.txt", "r", encoding='utf-8-sig')
province = province.read().split('\n')
provinceY = open("provinceY.txt", "r", encoding='utf-8-sig')
provinceY = provinceY.read().split('\n')
evaluation_form['eval'] = {'greet': sayhi,
                           'answer': answer,
                           'ques': ques,
                           'wordap': wordappende,
                           'qq2': qq2,
                           'number': number,
                           'province': province,
                           'provinceY': provinceY}
sayhay  = 'สวัสดีจ้าาา มาม่ะ มาคุยกับกอดอุ่นก่อน'
questionja = 'อยากจะเริ่มทำเเบบประเมินเลยหรืออยากจะคุยกับกอดอุ่น ก่อนนะ ถ้าอยากจะเริ่มทำเลยให้บอกว่า "เริ่มเลย" ถ้าอยากคุยต่อให้พิมพ์ว่า "คุยต่อ"'


def regular1(userid,question):
    i = 0
    count = 0
    while(i<len(sayhi)):
        pattern1 = r'[a-zA-Zก-๙เ' ']+('+sayhi[i]+')[a-zA-Zก-๙เ' ']+$'
        pattern2 = r'('+sayhi[i]+')[a-zA-Zก-๙เ' ']+$'    
        pattern3 = r'[a-zA-Zก-๙เ' ']+('+sayhi[i]+')$'
        pattern4 = r'('+sayhi[i]+')$'
        if re.search(pattern1,question):
            count = 1
        elif re.search(pattern2,question):
            count = 1
        elif re.search(pattern3,question):
            count = 1
        elif re.search(pattern4,question):
            count = 1
        i = i+1
    if count == 1:
        return "reg1"
    
def regular2(userid,question):
    i = 0
    count = 0
    while(i<len(ques)):
        pattern1 = r'[a-zA-Zก-๙เ]+('+ques[i]+')[a-zA-Zก-๙เ]+$'
        pattern2 = r'('+ques[i]+')[a-zA-Zก-๙เ]+$'    
        pattern3 = r'[a-zA-Zก-๙เ]+('+ques[i]+')$'
        pattern4 = r'('+ques[i]+')$'
        if re.search(pattern1,question):
            count = 1
        elif re.search(pattern2,question):
            count = 1
        elif re.search(pattern3,question):
            count = 1
        elif re.search(pattern4,question):
            count = 1
        i = i+1
    if count == 1:
        return "reg2"
    
        
        
        
        
        
        
        
        
        
        
        
        
        
