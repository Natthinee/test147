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
    pattern1 = '[ก-ฮ]('+evaluation_form['eval']['greet']+')[ก-ฮ]'
    pattern2 = '('+evaluation_form['eval']['greet']+')[ก-ฮ]'    
    pattern3 = '[ก-ฮ]('+evaluation_form['eval']['greet']+')'
    if question in pattern1 or pattern2 or pattern3:
        return sayhay
    
def regular2(userid,question):
  pattern1 = r'[a-zA-Zก-๙เ]+('+str(evaluation_form['eval']['ques'])+')[a-zA-Zก-๙เ]+$'
  pattern2 = r'('+str(evaluation_form['eval']['ques'])+')[a-zA-Zก-๙เ]+$'    
  pattern3 = r'[a-zA-Zก-๙เ]+('+str(evaluation_form['eval']['ques'])+')$'
  pattern4 = r'('+str(evaluation_form['eval']['ques'])+')$'
  if re.search(pattern1,question):
      return "k"
  elif re.search(pattern2,question):
      return "h"
  elif re.search(pattern3,question):
      return "i"
  elif re.search(pattern4,question):
      return "m"
    
        
        
        
        
        
        
        
        
        
        
        
        
        
