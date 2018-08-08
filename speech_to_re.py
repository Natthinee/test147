# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 23:42:26 2018

@author: Natthinee
"""

import speech_recognition as sr
import re
r = sr.Recognizer()
#with sr.WavFile("C:\\Users\\Natthinee\\Desktop\\แปลงเสียง\\00005.wav") as source:              # ใช้ "test.wav"  เป็นแหล่งให้ข้อมูลเสียง
  #audio = r.record(source)                        # ส่งข้อมูลเสียงจากไฟล์
#try:
  #print("Transcription: " + r.recognize_google(audio,language = "th-TH"))   # แสดงข้อความจากเสียงด้วย Google Speech Recognition
#except sr.RequestError as e:                                 # ประมวลผลแล้วไม่รู้จักหรือเข้าใจเสียง
  #print("Could not understand audio")
  
word = ['ปวดเเขน','ปวดขา']  

def speechword(filename):
    r = sr.Recognizer()
    with sr.WavFile(filename) as source:              # ใช้ "test.wav"  เป็นแหล่งให้ข้อมูลเสียง
      audio = r.record(source)                        # ส่งข้อมูลเสียงจากไฟล์
    try:
      return  r.recognize_google(audio,language = "th-TH")   # แสดงข้อความจากเสียงด้วย Google Speech Recognition
    except sr.RequestError as e:                                 # ประมวลผลแล้วไม่รู้จักหรือเข้าใจเสียง
      return "ไม่เจอ"
 
    
def speechcheck(filename):
    word = ['ปวดเเขน','ปวดขา']  
    i = 0
    count = 0
    filename = speechword(filename)
    while(i<len(word)):
        pattern1 = r'[a-zA-Zก-๙เ' ']+('+word[i]+')[a-zA-Zก-๙เ' ']+$'
        pattern2 = r'('+word[i]+')[a-zA-Zก-๙เ' ']+$'    
        pattern3 = r'[a-zA-Zก-๙เ' ']+('+word[i]+')$'
        pattern4 = r'('+word[i]+')$'
        if re.search(pattern1,filename):
            count = 1
        elif re.search(pattern2,filename):
            count = 1
        elif re.search(pattern3,filename):
            count = 1
        elif re.search(pattern4,filename):
            count = 1
        i = i+1
    if count == 1:
        return "reg4"