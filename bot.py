# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 20:11:32 2018

@author: Natthinee
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:31:06 2018
@author: Natthinee
"""
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,
                            SourceUser, SourceGroup, SourceRoom,
                            TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
                            ButtonsTemplate, URITemplateAction, PostbackTemplateAction,
                            CarouselTemplate, CarouselColumn, PostbackEvent,
                            StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
                            ImageMessage, VideoMessage, AudioMessage,
                            UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent)
from flask.ext.pymongo import PyMongo 
import pymongo
from pymongo import MongoClient
import json
import random
from province1 import Latitudee,longtitutee,hospitalName,provincee,addressPro
from countSco import scoreC,scoreQ2
from test import find1,find2,find3,findx,findy,findxy,findxx,findyy,deleteQu
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
listQNo = 'กอดอุ่นยังอ่อนหัด\nเด่วกอดอุ่นจะค่อยๆ เรียนรู้นะจ๊ะ\nพิมพ์ใหม่เนอะพิมพ์ใหม่'
richmanu = {}
richmanu['rich'] = {'rich01': 'เล่าหน่อยนะ',
                   'rich02': 'คุยกับเเบบประเมิน',
                   'rich03': 'ซึมเศร้าน่ารู้',
                   'rich04': 'จิตเวชใกล้บ้าน',
                   'rich05': 'เศร้าเเล้วเปลี่ยน',
                   'rich06': 'ข่าวสารซึมเศร้า'}
ansrich01 = ' เอ๊ะๆ อยากจะพิมพ์หรืออยากพูดน้าาา\nถ้าอยากจะพิมพ์เพื่อระบายก็มาเริ่มกันเลย\nเเต่ถ้าอยากจะพูดเพื่อระบายกดที่ปุ่มไมโครโฟนข้างๆได้เลยน้าา\nระบายมาได้เลยน้าา กอดอุ่นอยากฟัง ｡◕‿◕｡' ######
ansrich02 = 'ถ้า พร้อมเเล้วมาลุยกันเล้ยยย !!ミ●﹏☉'
ansrich03 = 'นี่ๆ อยากรู้อะไรบ้างเอ่ยเกี่ยวกับโรคซึมเศร้า ถามมาได้เลยน้าา ถ้ากอดอุ่นรู้ได้คำตอบเเน่นอน （´◔౪◔）'
ansrich04 = 'อยู่จังหวัดไหนเอ่ย ????? ۩۩۩۩'
ansrich05 = 'กอดอุ่นมีวิธีเบื้องต้นในการจัดการกับอารมณ์ เมื่อเกิดอาการซึมเศร้าลองทำตามดูน้าาา อาจการซึมเศร้าอาจจะน้อยลงก็ได้ ☺☻ '
ansrich06 = 'สามารถติดตามข่าวสารของโรคซึมเศร้าต่างๆ ได้ตามช่องทางข้างล่างนี้เลยน้าา ☜♥☞'
ans2 = ['มี','ไม่มี']
anss = ['ทำไรได้บ้าง','ทำไรได้','ทำไรได้บ้างอ่ะ','กอดอุ่นทำไรได้บ้างอ่ะ','เธอทำไรได้บ้างอ่ะ']
tess = 'สวัสดีจ้าา วันนี้มีอะไรอยากจะเม้าส์กับกอดอุ่นไหมเอ่ย?◑０◐\n เอ๊ะ!! หรือจะลองกดใช้งาน\nฟังก์ชันด้านล่างก็จิ้มที่ปุ่ม ">" สีเขียวได้เลยน้าา'
hos = 'ลองไปปรึกษากับกับจิตเเพทย์\nใกล้ๆบ้านดูน้าา'
game = 'พักสมองสักเเปบดีกว่าน้าา กอดอุ่นมีเกมส์มาให้เล่น สนใจไหม（´◔౪◔）'
app = Flask(__name__)

line_bot_api = LineBotApi('IzXs2WdxBaxjM/BTdVQ43pEYgt1O8BRRrEAOztjHPMfRUmM0BYtD4VRZg7MLMSyi1mWqI3vdPl08HfmsCUiBM1QJKc0OF89EfbEPIHEG+pKHO85//3Zvo+Qcf9MDZoFwe2m+cjasnyvwYZ3xPQNWPgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0dc428295a377a2e3ee1bda97af613e2')
app.config['MONGO_DBNAME'] = 'khim'
app.config['MONGO_URI'] = 'mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim'
mongo = PyMongo(app)
slope ='สรุปแบบประเมิน 9 คำถาม'
slope2 ='สรุปแบบประเมิน 2 คำถาม'
lo = ['มี.','ไม่มี.']
clock = ['ซ้าย','ขวา','ข้างซ้าย','ข้างขวา','ฝั่งซ้าย','ฝั่งขวา','ด้านซ้าย','ด้านขวา']
happy = ['ก็ดี','ก็เรื่อยๆ','ดี','ดีนะ','มีความสุขดี','มีความสุข','ธรรมดา','ไม่ทุกข์อ่ะ','ก็ดีนะ','ไม่ได้พิเศษอะไร','เหมือนทุกวันอ่ะ','ฉันสวย','สวย','น่ารัก','เหมือนทุกวัน','มีความสุขดีจ้า','เราน่ารักม่ะ','น่ารักม่ะ','รู้สึกสวยจัง']
unhappy = ['มีเเรื่องทุกข์ใจ','ทุกข์ใจ','เบื่อ','หงุดหงิด','ไม่อยากมีชีวิตอยู่เเล้ว','ไม่อยากมีชีวิต','ไม่อยากออกไปไหน','น้ำหนักฉันลด','น้ำหนักลด','น้ำหนักขึ้น','ไม่มีความสุข','เก็บกด','อึดอัดใจ','อึดอัด','น่าเบื่อ','น่ารำคาญจัง','น่าหงุดหงิด','ไม่สดใส','ไม่ร่าเริง']
sayhappy = ['เคร','ลองดู','ได้ๆ','เอามาดิ','ลองดูก็ได้','ได้','ได้นะ','ok','Ok','โอเค','ตกลง','ได้จ้า','เครนะ','ตกลง','โอเครร','โอเคร']
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
    client = MongoClient('mongodb://khimmy:Kk2047849@ds147030.mlab.com:47030/khim')
    db  = client.khim.user
    dd  = client.khim.Q2
    #print(count)
    #if question in 'สวัสดีจ้าาา':
       #answer = tess 
       #sticker_message = StickerSendMessage(
       #package_id='1',
       #sticker_id='2')
       #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
       #line_bot_api.push_message(userid, sticker_message)  
        
    if question in 'ขิม':
        answer = str(find1(userid,question))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    if question in 'วิม':
        answer = str(find2(userid,question))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    if question in 'ภีม':
        answer = str(find3(userid,question))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    if question in 'ลี':
        answer = str(findx(userid,question))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    if question in 'วี':
        answer = str(findy(userid,question))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    if question in 'ไข่มุก':
        answer = str(findxy(userid,question))
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    if question in evaluation_form['eval']['greet']:
        answer = random.choice(evaluation_form['eval']['answer']) + 'วันนี้รู้สึกยังไงบ้างเอ่ย?'
        sticker_message = StickerSendMessage(
        package_id='2',
        sticker_id='22')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, sticker_message)
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=location_message))
    elif question in happy:
        answer = 'ฟังดูไม่น่าเป็นห่วงเท่าไหร่เนอะ กอดอุ่นมีเพลงกับนิยายมาเเนะนำลองฟังดูป่ะ'
        sticker_message = StickerSendMessage(
        package_id='1',
        sticker_id='125')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, sticker_message)
    elif question in sayhappy:
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                  CarouselColumn(
                      thumbnail_image_url='https://www.iphonemod.net/wp-content/uploads/2009/09/album-cover-01.png',
                      title='มาฟังเพลงผ่อนคลายกันดีกว่า',
                      text='มาฟังเพลงกัน',
                      actions=[      
                            URITemplateAction(
                                label='Not Spring',
                                uri='https://www.youtube.com/watch?v=ouR4nn1G9r4&start_radio=1&list=RDouR4nn1G9r4'
                            ), 
                            URITemplateAction(
                                label='ความต่าง',
                                uri='https://www.youtube.com/watch?v=my7XIjUslLw'
                            ),
                            URITemplateAction(
                                label='มะงึกๆอุ๋งๆ',
                                uri='https://www.youtube.com/watch?v=HI4voGt6LLM'
                            )
                         ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://s.isanook.com/pn/0/rp/rc/w200h267/ya0xa0m1w0/aHR0cHM6Ly9zLmlzYW5vb2suY29tL3BuLzAvdWQvMTQvNzA1NTAvNzA1NTAtdGh1bWJuYWlsLTIwMTgwNjI1MjMwMDAyLnBuZw==.png',
                        title='มารักการอ่านกัน',
                        text='อ่านกันถอะ',
                        actions=[
                            URITemplateAction(
                                label='การ์ตูนคลายเครียด',
                                uri='https://today.line.me/th/pc/article/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%95%E0%B8%B9%E0%B8%99%E0%B8%84%E0%B8%A5%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%94%E0%B8%AA%E0%B8%B8%E0%B8%94%E0%B8%A5%E0%B8%B1%E0%B9%88%E0%B8%99+%E0%B8%82%E0%B8%99%E0%B8%82%E0%B8%9A%E0%B8%A7%E0%B8%99%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%AE%E0%B8%B2%E0%B8%A1%E0%B8%B2%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B8%AD%E0%B9%88%E0%B8%B2%E0%B8%99%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%96%E0%B8%B6%E0%B8%87%E0%B8%97%E0%B8%B5%E0%B9%88+%E0%B8%94%E0%B8%B9%E0%B9%81%E0%B8%A5%E0%B9%89%E0%B8%A7%E0%B8%A1%E0%B8%B5%E0%B8%82%E0%B8%B3+%E0%B8%A5%E0%B8%B1%E0%B9%88%E0%B8%99%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B9%81%E0%B8%99%E0%B9%88%E0%B8%99%E0%B8%AD%E0%B8%99-lZjQpW'
                            ),
                            URITemplateAction(
                                label='เว็บตูน',
                                uri='https://www.webtoons.com/th/'
                            ),
                            URITemplateAction(
                                label='comico',
                                uri='http://www.comico.in.th/'
                            )
                        ]
                    )
                 ]
              )
          )
      
        #bot()
        #location_message = LocationSendMessage(
        #title='my location',
        #address='Tokyo',
        #latitude=35.65910807942215,
        #longitude=139.70372892916203)
        #line_bot_api.push_message(userid, location_message)
      
        ##answer = ansrich03
        #message = gg(uestion)
        ##userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        #line_bot_api.reply_message(event.reply_token, msgs)
        line_bot_api.reply_message(event.reply_token,  carousel_template_message)
    elif question in 'ทำต่อ':
        #questi = str(find1(userid,question))
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = str(find1(userid,question)),
                text='เลือกข้อมูลตามระดับอาการนะจ๊ะ',
                actions=[
                    MessageTemplateAction(
                        label='0=ไม่มีเลย',
                        text='0',
                    ),
                    MessageTemplateAction(
                        label='1=เป็นบางวัน',
                        text='1'
                    ),
                    MessageTemplateAction(
                        label='2=เป็นบ่อย',
                        text='2'
                    ),
                    MessageTemplateAction(
                        label='3=เป็นทุกวัน',
                        text='3'
                    )
                ]
             )
          )
        
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    
    elif question  in evaluation_form['eval']['ques']:
        confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
               text='มาทำเเบบประเมินกันดีกว่า',
               actions=[
                    MessageTemplateAction(
                        label='เริ่มทำ',
                        text='เริ่มทำ'
                    ),
                    MessageTemplateAction(
                        label='ฟังก์ชันเพิ่มเติม',
                        text='ฟังก์ชันเพิ่มเติม'
                    )
               ]
            )
        )
        #print("confirm_template_message")        
        #print(confirm_template_message)
        
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
    elif question  in 'เริ่มทำ':
        confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
               text=str(find2(userid,question)),
               actions=[
                    MessageTemplateAction(
                        label='มี',
                        text='มี'
                    ),
                    MessageTemplateAction(
                        label='ไม่มี',
                        text='ไม่มี'
                    )
               ]
            )
        )
        #print("confirm_template_message")        
        #print(confirm_template_message)
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
    elif question  in ans2:
        if(question in ans2):
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text=str(find2(userid,question)),
                    actions=[
                        MessageTemplateAction(
                            label='มี',
                            text='มี.'
                        ),
                        MessageTemplateAction(
                            label='ไม่มี',
                            text='ไม่มี.'
                        )
                     ]
                  )
               )
        #print("confirm_template_message")        
        #print(confirm_template_message)
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
    elif question in 'ทำไรได้บ้าง':
        #question1 = str(find1(userid,question))
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=question1))
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='สิ่งที่กอดอุ่นสามารถทำได้',
                text='ลองเลือกดูซิ',
                actions=[
                    MessageTemplateAction(
                        label='เล่าหน่อยนะ',
                        text='เล่าหน่อยนะ',
                    ),
                    MessageTemplateAction(
                        label='คุยกับเเบบประเมิน',
                        text='คุยกับเเบบประเมิน'
                    ),
                    MessageTemplateAction(
                        label='จิตเวชใกล้บ้าน',
                        text='จิตเวชใกล้บ้าน'
                    ),
                    MessageTemplateAction(
                        label='ฟังก์ชันเพิ่มเติม',
                        text='ฟังก์ชันเพิ่มเติม'
                    )
                ]
             )
          )
        
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    
    elif question in 'ฟังก์ชันเพิ่มเติม':
        #question1 = str(find1(userid,question))
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=question1))
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='กอดอุ่นทำได้ๆ',
                text='ลองเลือกใช้ดูหน่อยนะจ๊ะ',
                actions=[
                    MessageTemplateAction(
                        label='ซึมเศร้าน่ารู้',
                        text='ซึมเศร้าน่ารู้',
                    ),
                    MessageTemplateAction(
                        label='เศร้าเเล้วเปลี่ยน',
                        text='เศร้าเเล้วเปลี่ยน'
                    ),
                    MessageTemplateAction(
                        label='ข่าวสารซึมเศร้า',
                        text='ข่าวสารซึมเศร้า'
                    ),
                    MessageTemplateAction(
                        label='สรุปเเบบประเมิน',
                        text='สรุปเเบบประเมิน'
                    )
                ]
             )
          )
        
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    
    elif question in 'สรุปแบบประเมิน':
        answer = str(scoreC(userid,question))+'\n' + '\n'+str(scoreQ2(userid,question))
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='ลองใช้ฟังก์ชันอื่นดูได้น้าา',
                text='ลองเลือกดูซิ',
                actions=[
                    MessageTemplateAction(
                        label='เล่าหน่อยนะ',
                        text='เล่าหน่อยนะ',
                    ),
                    MessageTemplateAction(
                        label='เริ่มทำเเบบประเมินใหม่',
                        text='เริ่มทำเเบบประเมินใหม่'
                    ),
                    MessageTemplateAction(
                        label='จิตเวชใกล้บ้าน',
                        text='จิตเวชใกล้บ้าน'
                    ),
                    MessageTemplateAction(
                        label='ฟังก์ชันเพิ่มเติม',
                        text='ฟังก์ชันเพิ่มเติม'
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    #elif question in evaluation_form['eval']['ques']:
        #question1 = str(find1(userid,question)) ######test#####
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=question1))
    elif question in number:
        #question1 = str(find1(userid,question))
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=question1))
        answer = str(find1(userid,question))
        score = str(findxx(userid,question))
        if(score == '10'):
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text= 'ทำไรต่อดีน้าา',
                    actions=[
                        MessageTemplateAction(
                            label='ฟังก์ชันเพิ่มเติม',
                            text='ฟังก์ชันเพิ่มเติม'
                        ),
                        MessageTemplateAction(
                            label='สรุปแบบประเมิน',
                            text='สรุปแบบประเมิน'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, confirm_template_message)
          
        if(question in number):              
            buttons_template_message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    title=answer,
                    text='เลือกข้อมูลตามระดับอาการนะจ๊ะ',
                    actions=[
                        MessageTemplateAction(
                            label='0=ไม่มีเลย',
                            text='0',
                        ),
                        MessageTemplateAction(
                            label='1=เป็นบางวัน',
                            text='1'
                        ),
                        MessageTemplateAction(
                            label='2=เป็นบ่อย',
                            text='2'
                        ),
                        MessageTemplateAction(
                            label='3=เป็นทุกวัน',
                            text='3'
                        )
                    ]
                )
            )
        
            line_bot_api.reply_message(event.reply_token, buttons_template_message)
    
    #elif question in ans2:
        #question1 = str(find1(userid,question))
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=question1))  
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
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                  CarouselColumn(
                      thumbnail_image_url='https://www.bangkokhospital.com/assets/content/b09222762aff1689c735642ed30d6d31.jpg',
                      title='โรคซึมเศร้าคืออะไร?',
                      text='ทำความเข้าใจโรคซึมเศร้า',
                      actions=[     
                          URITemplateAction(
                              label='รู้จักกับโรคซึมเศร้า',
                              uri='https://www.honestdocs.co/most-common-psychiatric-disorders'
                          ),
                          URITemplateAction(
                              label='โลกที่เปลี่ยนไป',
                              uri='https://www.seedoctornow.com/depression-expression'
                          ),
                          URITemplateAction(
                              label='รู้เรื่องโรคซึมเศร้า',
                              uri='http://www.thaifamilylink.net/web/node/29'
                          )
                       ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.ytimg.com/vi/w7QZKCJTw2o/maxresdefault.jpg',
                        title='จับสังเกต "โรคซึมเศร้า"',
                        text='มีอาการหลักคือ',
                        actions=[
                            URITemplateAction(
                                label='จับสังเกต',
                                uri='https://www.youtube.com/watch?v=w7QZKCJTw2o'
                            ),
                            URITemplateAction(
                                label='ซึมเศร้าบนออนไลน์',
                                uri='http://www.healthtodaythailand.net/%E0%B8%88%E0%B8%B1%E0%B8%9A%E0%B8%AA%E0%B8%B1%E0%B8%8D%E0%B8%8D%E0%B8%B2%E0%B8%93%E0%B9%82%E0%B8%A3%E0%B8%84%E0%B8%8B%E0%B8%B6%E0%B8%A1%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B9%89%E0%B8%B2/'
                            ),
                            URITemplateAction(
                                label='9สัญญาณเตือน',
                                uri='https://www.bangkokhospital.com/index.php/th/diseases-treatment/major-depressive-disorder'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://pbs.twimg.com/media/DdiKlOYU0AALw5I.jpg',
                        title='โรคซึมเศร้ากับอารณ์ซึมเศร้า',
                        text='ความเหมือนที่เเตกต่างกัน',
                        actions=[
                            URITemplateAction(
                                label='เครียดและโรคซึมเศร้า',
                                uri='http://haamor.com/th/%E0%B8%A0%E0%B8%B2%E0%B8%A7%E0%B8%B0%E0%B8%8B%E0%B8%B6%E0%B8%A1%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B9%89%E0%B8%B2'
                            ),
                            URITemplateAction(
                                label='ความเครียดเเละซึมเศร้า',
                                uri='https://nuuneoi.com/blog/blog.php?read_id=716'
                            ),
                            URITemplateAction(
                                label='6ข้อเเตกต่าง',
                                uri='https://today.line.me/th/pc/article/6+%E0%B8%82%E0%B9%89%E0%B8%AD%E0%B9%81%E0%B8%95%E0%B8%81%E0%B8%95%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B8%A3%E0%B8%B0%E0%B8%AB%E0%B8%A7%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B9%82%E0%B8%A3%E0%B8%84%E0%B8%8B%E0%B8%B6%E0%B8%A1%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B9%89%E0%B8%B2-0946b58ae2a7e66fcba53b041348eed590c786627626de0061a2dd9bca071064'
                           )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://gedgoodlife.pi.bypronto.com/2/wp-content/uploads/sites/2/2017/08/902-depression-1.jpg', 
                        title='โรคซึมเศร้ารักษาได้',
                        text='รู้เท่าทันก่อนจะสาย',
                        actions=[
                            URITemplateAction(
                                label='การรักษา',
                                uri='https://www.pobpad.com/%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A3%E0%B8%B1%E0%B8%81%E0%B8%A9%E0%B8%B2%E0%B9%82%E0%B8%A3%E0%B8%84%E0%B8%8B%E0%B8%B6%E0%B8%A1%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B9%89%E0%B8%B2'
                            ),
                            URITemplateAction(
                                label='รักษาโดยธรรมชาติ',
                                uri='https://th.wikihow.com/%E0%B8%A3%E0%B8%B1%E0%B8%81%E0%B8%A9%E0%B8%B2%E0%B8%AD%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%8B%E0%B8%B6%E0%B8%A1%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B9%82%E0%B8%94%E0%B8%A2%E0%B8%98%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%8A%E0%B8%B2%E0%B8%95%E0%B8%B4'
                            ),
                            URITemplateAction(
                                label='การรักษาทางเลือก',
                                uri='https://www.bbc.com/thai/40115831'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.schoolofchangemakers.com/sites/default/files/82caca80957a300e812dbb52876ee5b4.jpg',
                        title='วิธีกระชับความเศร้า',
                        text='วิธีกระชับความเศร้า',
                        actions=[
                            URITemplateAction(
                                label='คนใกล้ชิด',
                                uri='https://www.choojaiproject.org/2017/07/helping-a-friend-through-the-darkness-of-depression/'
                            ),
                            URITemplateAction(
                                label='วิธีก้าวผ่าน',
                                uri='https://thestandard.co/coverstory3/'
                            ),
                            URITemplateAction(
                                label='เพื่อนเรา(ซึม)เศร้า',
                                uri='http://www.thaiticketmajor.com/variety/lifestyle/9371/'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.ytimg.com/vi/Gs6ufPBtS0A/maxresdefault.jpg',
                        title='ประสบการณ์โรคซึมเศร้า',
                        text='รีวิวโรคซึมเศร้า',
                        actions=[
                            URITemplateAction(
                                label='ภาวะซึม',
                                uri='https://www.youtube.com/watch?v=H5sUpGv68LE'
                            ),
                            URITemplateAction(
                                label='รีวิวทราย เจริญปุระ',
                                uri='https://www.youtube.com/watch?v=kwElbde56o0'
                            ),
                            URITemplateAction(
                                label='รีวิวขุนเขา สินธุเสน',
                                uri='https://www.youtube.com/watch?v=DPFhoK92xuw'
                            )
                        ]
                    )
                  ]
              )
          )
      
        #bot()
        #location_message = LocationSendMessage(
        #title='my location',
        #address='Tokyo',
        #latitude=35.65910807942215,
        #longitude=139.70372892916203)
        #line_bot_api.push_message(userid, location_message)
      
        ##answer = ansrich03
        #message = gg(uestion)
        ##userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        #line_bot_api.reply_message(event.reply_token, msgs)
        line_bot_api.reply_message(event.reply_token,  carousel_template_message)
    elif question == richmanu['rich']['rich04']:
        answer = ansrich04
        ##userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    elif question in evaluation_form['eval']['province']:
        answer = hos+'\n'+str(addressPro(question))
        location_message = LocationSendMessage(
        title = provincee(question),
        address = hospitalName(question),
        latitude = Latitudee(question),
        longitude = longtitutee(question) )
        sticker_message = StickerSendMessage(
        package_id='2',
        sticker_id='176')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, location_message)
        line_bot_api.push_message(userid, sticker_message)
        
    elif question == richmanu['rich']['rich05']:
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                  CarouselColumn(
                      thumbnail_image_url='https://i1.wp.com/lightmeup.me/wp-content/uploads/2016/01/strong.png',
                      title='กิจกรรมทำเเล้วคลายเครียด',
                      text='ทำให้ใจสบายเเละผ่อนคลายกันเถอะ',
                      actions=[      
                            URITemplateAction(
                                label='4วิธีง่ายๆปรับสภาพจิตใจ',
                                uri='https://www.hongthongrice.com/life/5986/4feelgood/'
                            ), 
                            URITemplateAction(
                                label='7กิจกรรมคลายเครียด',
                                uri='http://sukkaphap-d.com/7-%E0%B8%81%E0%B8%B4%E0%B8%88%E0%B8%81%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%84%E0%B8%A5%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%94-%E0%B9%80%E0%B8%9E%E0%B8%B4%E0%B9%88/'
                            ),
                            URITemplateAction(
                                label='9กิจกรรมคลายเศร้า',
                                uri='http://www.jeban.com/topic/239807'
                            )
                         ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://fb1-dz.lnwfile.com/wa6rdl.png',
                        title='ปรับสติให้ผ่อนคลาย',
                        text='สร้างจิตให้ผ่อนคลายกัน',
                        actions=[
                            URITemplateAction(
                                label='วิธีการผ่อนคลายจิตใจ',
                                uri='https://th.wikihow.com/%E0%B8%9C%E0%B9%88%E0%B8%AD%E0%B8%99%E0%B8%84%E0%B8%A5%E0%B8%B2%E0%B8%A2%E0%B8%88%E0%B8%B4%E0%B8%95%E0%B9%83%E0%B8%88'
                            ),
                            URITemplateAction(
                                label='ฝึกผ่อนคลายความเครียด',
                                uri='https://www.dmh.go.th/news/view.asp?id=1012'
                            ),
                            URITemplateAction(
                                label='การขจัดทุกข์ด้วยตนเอง',
                                uri='https://www.dmh.go.th/news/view.asp?id=1006'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://png.pngtree.com/element_origin_min_pic/00/09/45/3156a0892691dab.jpg',
                        title='ออกกำลังกายสร้างกำลังใจ',
                        text='ขยับวันละนิดปรับเปลี่ยนชีวิตสดใส',
                        actions=[
                            URITemplateAction(
                                label='3ท่าโยคะก่อนนอน',
                                uri='https://www.pf.co.th/blog/cozy-at-home/fit-at-home/2017/07/07/yoga-at-home/'
                            ),
                            URITemplateAction(
                                label='วิ่งแล้วดี',
                                uri='https://blog.thai.run/%E0%B8%A7%E0%B8%B4%E0%B9%88%E0%B8%87%E0%B9%81%E0%B8%A5%E0%B9%89%E0%B8%A7%E0%B8%94%E0%B8%B5%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B8%99%E0%B8%B5%E0%B9%89%E0%B8%99%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%AD%E0%B8%87-31fbd88fd2ca'
                            ),
                            URITemplateAction(
                                label='9กีฬาทางเลือก',
                                uri='https://www.honestdocs.co/9-alternative-sports-exercise-not-boring'
                            )
                        ]
                    )
                 ]
              )
          )
      
        #bot()
        #location_message = LocationSendMessage(
        #title='my location',
        #address='Tokyo',
        #latitude=35.65910807942215,
        #longitude=139.70372892916203)
        #line_bot_api.push_message(userid, location_message)
      
        ##answer = ansrich03
        #message = gg(uestion)
        ##userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        #line_bot_api.reply_message(event.reply_token, msgs)
        line_bot_api.reply_message(event.reply_token,  carousel_template_message)
 
    elif question == richmanu['rich']['rich06']:
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                  CarouselColumn(
                      thumbnail_image_url='https://obs.line-scdn.net/0hoxh888FeMFdVQRxh4rRPAG8XMzhmLSNUMXdhVAkvbmModXdSOXd8YnlDbjIrcncJO3R7M3JGK2Z-eCJVaS98/w644',
                      title='ติดตามในเเฟนเพจ',
                      text='แฟนเพจ',
                      actions=[     
                            URITemplateAction(
                                label='คลินิกสุขภาพจิต',
                                uri='https://www.facebook.com/D2JED/'
                            ),
                            URITemplateAction(
                                label='สายด่วน1323',
                                uri='https://www.facebook.com/helpline1323/'
                            ),
           
                            URITemplateAction(
                                label='จิตแพทย์แห่งประเทศไทย',
                                uri='https://www.facebook.com/ThaiPsychiatricAssociation/'
                            
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://s.isanook.com/he/0/ud/1/9229/sad.jpg',
                        title='ติดตามในเว็บไซต์',
                        text='ติดตามข่าวสาร',
                        actions=[ 
                            URITemplateAction(
                                label='สถาบันสุขภาพจิต',
                                uri='http://www.smartteen.net/main/'
                            ),
                            URITemplateAction(
                                label='กระทรวงสาธารณสุข',
                                uri='https://www.moph.go.th/'
                            ),
                            URITemplateAction(
                                label='ซึมเศร้าในต่างเเดน',
                                uri='https://www.webmd.com/depression/default.html'
                            )
                           
                         ]
                      )
                 ]
              )
          )
                    
      
        #bot()
        #location_message = LocationSendMessage(
        #title='my location',
        #address='Tokyo',
        #latitude=35.65910807942215,
        #longitude=139.70372892916203)
        #line_bot_api.push_message(userid, location_message)
      
        ##answer = ansrich03
        #message = gg(uestion)
        ##userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        #line_bot_api.reply_message(event.reply_token, msgs)
        line_bot_api.reply_message(event.reply_token,carousel_template_message)
    elif question in lo:
        confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
               text=str(find2(userid,question)),
               actions=[
                    MessageTemplateAction(
                        label='สนใจ',
                        text='สนใจ'
                    ),
                    MessageTemplateAction(
                        label='ทำต่อ',
                        text='ทำต่อ'
                    )
               ]
            )
        )
        #print("confirm_template_message")        
        #print(confirm_template_message)
        
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
    elif question in 'เริ่มทำเเบบประเมินใหม่':
        #del = deleteQu(userid,question)
        db.delete_many({'UserID':userid})
        dd.delete_many({'UserID':userid})
        confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
               text='มาทำเเบบประเมินกันดีกว่า',
               actions=[
                    MessageTemplateAction(
                        label='เริ่มทำ',
                        text='เริ่มทำ'
                    ),
                    MessageTemplateAction(
                        label='ฟังก์ชันเพิ่มเติม',
                        text='ฟังก์ชันเพิ่มเติม'
                    )
               ]
            )
        )
        #print("confirm_template_message")        
        #print(confirm_template_message)
        
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
      
    if question in 'สนใจ':
        image_message = ImageSendMessage(
            original_content_url='https://www.meekhao.com/wp-content/uploads/2018/02/puzzles-06.jpg',
            preview_image_url ='https://www.meekhao.com/wp-content/uploads/2018/02/puzzles-06.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
        
        
    elif question in clock:
        answer = 'เฉลย เรือนซ้ายจ้า เพราะถ้าเกิดนาฬิกาเดินเข็มวินาทีจะชนจ้าาา'+'\n'+'ถ้าจะทำต่อพิมพ์คำว่า "ทำต่อ"'+'\n'+'ถ้าอยากใช้ฟังก์ชันก์ใหม่ ให้พิมพ์ "ฟังก์ชันเพิ่มเติม" นะจ๊ะ'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
      
        
    
    else:
        answer = listQNo 
        #userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        sticker_message = StickerSendMessage(
        package_id='2',
        sticker_id='30')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, sticker_message)
        

if __name__ == "__main__":
    app.run()
