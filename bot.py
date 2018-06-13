# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:31:06 2018

@author: Natthinee
"""
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from flask.ext.pymongo import PyMongo
import pymongo
from pymongo import MongoClient
import json
import random
from test import find1
from app import bot
question1 = ''
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
evaluation_form['eval'] = {'greet': sayhi,
                           'answer': answer,
                           'ques': ques,
                           'wordap': wordappende,
                           'qq2': qq2,
                           'number': number}
listQNo = 'กอดอุ่น ยังอ่อนด๋อย กอดอุ่นยังไม่รู้ว่ากำลังพิมพ์อะไร ช่วยกอดอุ่นด้วยน้าา'
richmanu = {}
richmanu['rich'] = {'rich01': 'เล่าหน่อยนะ',
                   'rich02': 'คุยกับเเบบประเมิน',
                   'rich03': 'ซึมเศร้าน่ารู้',
                   'rich04': 'จิตเวชใกล้บ้าน',
                   'rich05': 'เศร้าเล้วเปลี่ยน',
                   'rich06': 'ข่าวสารซึมเศร้า'}
ansrich01 = ' เอ๊ะๆ อยากจะพิมพ์หรืออยากพูดน้าาา\nถ้าอยากจะพิมพ์เพื่อระบายก็มาเริ่มกันเลย\nเเต่ถ้าอยากจะพูดเพื่อระบายกดที่ปุ่มไมโครโฟนข้างๆได้เลยน้าา\nระบายมาได้เลยน้าา กอดอุ่นอยากฟัง ｡◕‿◕｡' ######
ansrich02 = 'ถ้า พร้อมเเล้วมาลุยกันเล้ยยย !!ミ●﹏☉'
ansrich03 = 'นี่ๆ อยากรู้อะไรบ้างเอ่ยเกี่ยวกับโรคซึมเศร้า ถามมาได้เลยน้าา ถ้ากอดอุ่นรู้ได้คำตอบเเน่นอน （´◔౪◔）'
ansrich04 = 'อยู่จังหวัดไหนเอ่ย ????? ۩۩۩۩'
ansrich05 = 'กอดอุ่นมีวิธีเบื้องต้นในการจัดการกับอารมณ์ เมื่อเกิดอาการซึมเศร้าลองทำตามดูน้าาา อาจการซึมเศร้าอาจจะน้อยลงก็ได้ ☺☻ '
ansrich06 = 'สามารถติดตามข่าวสารของโรคซึมเศร้าต่างๆ ได้ตามช่องทางข้างล่างนี้เลยน้าา ☜♥☞'
ans2 = ['มี','ไม่มี']

app = Flask(__name__)

line_bot_api = LineBotApi('IzXs2WdxBaxjM/BTdVQ43pEYgt1O8BRRrEAOztjHPMfRUmM0BYtD4VRZg7MLMSyi1mWqI3vdPl08HfmsCUiBM1QJKc0OF89EfbEPIHEG+pKHO85//3Zvo+Qcf9MDZoFwe2m+cjasnyvwYZ3xPQNWPgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0dc428295a377a2e3ee1bda97af613e2')
app.config['MONGO_DBNAME'] = 'khim'
app.config['MONGO_URI'] = 'mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim'
mongo = PyMongo(app)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def godaun(event):
    userr = mongo.db.user
    userid = event.source.user_id
    question = event.message.text
    if question in evaluation_form['eval']['greet']:
        answer = random.choice(evaluation_form['eval']['answer'] )
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    elif question in evaluation_form['eval']['ques']:
        question1 = str(find1(userid,question)) ######test#####
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=question1))
    elif question in number:
        question1 = str(find1(userid,question))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=question1))
    elif question in ans2:
        question1 = str(find1(userid,question))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=question1))  
    elif question == richmanu['rich']['rich01']:
        answer = ansrich01
        userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        #################################ส่วนนี้เด่วทำทีหลังสุด####################################################
    elif question == richmanu['rich']['rich02']:
        answer = ansrich02
        userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
      ##################################อยู่ในส่วนเดียวกับข้างบนเเละเเต่เผื่อฟังก์ชันก์เพิ่ม################################
    elif question == richmanu['rich']['rich03']:
        bot()
        ##answer = ansrich03
        #message = gg(uestion)
        ##userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        #line_bot_api.reply_message(event.reply_token, message)
        
    elif question == richmanu['rich']['rich04']:
        answer = ansrich04
        userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    elif question == richmanu['rich']['rich05']:
        answer = ansrich05
        userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    elif question == richmanu['rich']['rich06']:
        answer = ansrich06
        userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    else:
        answer = listQNo 
        #userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))

if __name__ == "__main__":
    app.run()
