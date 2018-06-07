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
listanswer = []
question1 = ''
face = ''
score = 0
sc = 0
qe = ''
faceqe = ''
appe = []
score = 0
number = ['0', '1', '2', '3']
qqq2 = []
q2q = ''
scc = 0
i = 0
evaluation_form = {}
number = ['0', '1', '2', '3']
sayhi = open("sayhi.txt", encoding='utf-8-sig')
sayhi = sayhi.read().split(',')
answer = open("answer.txt", "r", encoding='utf-8-sig')
answer = answer.read().split(',')
ques = open("Ques.txt", "r", encoding='utf-8-sig')
ques = ques.read().split(',')
quest9 = open("Quest9.txt", "r", encoding='utf-8-sig')
quest9 = quest9.read().split(',')
wordappende = open("wordappende.txt", "r", encoding='utf-8-sig')
wordappende = wordappende.read().split(',')
qq2 = open("qq2.txt", "r", encoding='utf-8-sig')
qq2 = qq2.read().split(',')
evaluation_form['eval'] = {'greet': sayhi,
                           'answer': answer,
                           'ques': ques,
                           'quest9': quest9,
                           'wordap': wordappende,
                           'qq2': qq2,
                           'number': number}
answer0123 = {}
answer0123['answer0123'] = {'answer0': 'ไม่มีเลย',
                            'answer1': 'เป็นบางวัน',
                            'answer2': 'เป็นบ่อย',
                            'answer3': 'เป็นทุกวัน'}
select2 = {}
select2['selc'] = {'selc01': 'มี',
                   'selc02': 'ไม่มี'}

please = {}
please['ple'] = {'ple': 'กรุณาพิมพ์หมายเลข 0 1 2 3 ตามระดับของอาการที่เป็นหน่อยน้าาา',
                 'ple1': 'พิมพ์ "มี" หน่อยนะถ้ามีอาการ พิมพ์ "ไม่มี" ถ้าไม่มีอาการน้าาา',
                 'ple2': 'กรุณาตอบ "ไม่มี" ถ้าไม่มีอาการ หรือตอบ "มี" ถ้าไม่มีอาการ',
                 'ple3': 'กรุณาตอบ "ได้" หากสามารถควบคุมอารมณ์ตัวเองได้ ตอบ "ไม่ไ้ด้" หากท่านไม่สามารถควบคุมอารมณ์ตนเองได้',
                 'Error': '-- เอ๊ะ! พิมพ์ผิดหรือเปล่าน้าาาา กอดอุ่นไม่เห็นเข้าใจเลย :/'}
setscoreq9 = {}
setscoreq9['score'] = {'pprint': ' 0 = ไม่มีเลย\n 1 = เป็นบางวัน\n 2 = เป็นบ่อย\n 3 = เป็นทุกวัน\n'}
quest8 = {}
quest8['quest8'] = {'quest01': 'มีความคิดอยากตาย หรือคิดว่าตายไปจะดีกว่า',
                    'quest02': 'อยากทำร้ายตัวเอง หรือทำให้ตัวเองบาดเจ็บ',
                    'quest03': 'มีความคิดเกี่ยวกับการฆ่าตัวตาย',
                    'quest031': 'ท่านสามารถควบคุมความอยากฆ่าตัวตายที่ท่านคิดอยู่นั้นได้หรือไม่ หรือบอกได้ไหมว่าคงจะไม่ทำตามความคิดนั้นในขณะนี้',
                    'quest04': 'มีแผนการที่จะฆ่าตัวตาย',
                    'quest05': 'ได้เตรียมการที่จะทำร้ายตนเอง หรือเตรียมการจะฆ่าตัวตาย โดยตั้งใจว่าจะให้ตายจริงๆ',
                    'quest06': 'ได้ทำให้ตนเองบาดเจ็บ แต่ไม่ตั้งใจที่จะทำให้เสียชีวิต',
                    'quest07': 'ได้พยายามฆ่าตัวตาย โดยคาดหวัง/ตั้งใจที่จะให้ตาย',
                    'quest08': 'ตลอดชีวิตที่ผ่านมา... ท่านเคยพยายามฆ่าตัวตาย'}
ans8 = {}
ans8['ans'] = {'an': 'ไม่ได้',
               'ay': 'ได้'}
listQ = ''


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
def movie(event):
    userr = mongo.db.user
    if event.message.text in evaluation_form['eval']['greet']:
        question = event.message.text
        answer = random.choice(evaluation_form['eval']['answer'] )    
        userr.insert({"Question": question, "Answer": answer})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    elif event.message.text in evaluation_form['eval']['ques']:
        question = event.message.text
        question1 = random.choice(evaluation_form['eval']['quest9'])
        face = random.choice(evaluation_form['eval']['wordap'])
        answer = face + question1 +'\n'+ setscoreq9['score']['pprint']+'\n'+ please['ple']['ple']
        listanswer.append(question)
        userr.insert({"Question": question, "Answer": question})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    elif event.message.text in number:
        question = event.message.text
        question1 = random.choice(evaluation_form['eval']['quest9'])
        face = random.choice(evaluation_form['eval']['wordap'])
        answer = face + question1 +'\n'+ setscoreq9['score']['pprint']+'\n'+ please['ple']['ple']
        listanswer.append(question)
        userr.insert({"Question": question, "Answer": answer})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
      
        
        
        
        
        



if __name__ == "__main__":
    app.run()
