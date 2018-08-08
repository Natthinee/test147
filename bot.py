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

import os
import sys
import tempfile
import binascii
from argparse import ArgumentParser
import boto3
import boto
import moto
from boto3.s3.transfer import TransferConfig
from boto3.session import Session
from argparse import ArgumentParser
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
from pymongo import MongoClient
from flask_pymongo import PyMongo
import pymongo
import json
import random
import re
from province1 import Latitudee,longtitutee,hospitalName,provincee,addressPro,namehosLati,namehosLong,provinceehos,addressProhos,hospiName,hospro1,hospro2,tud2prov,tud21,tud22
from countSco import scoreC,scoreQ2,scorephoto,scoreme2
from Querry import find1,find2,find3,findx,findy,findxy,findxx,findyy,deleteQu,continues
from regularCheck import regular1,regular2,regular3,regular4,regular5,regular6,regular7
from provincenotmap import provincenot4,provincenot3,provincenot2,provincenot1
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
NameHospital = open("NameHospital.txt", "r", encoding='utf-8-sig')
NameHospital = NameHospital.read().split('\n')
prohos2pro = open("prohos2pro.txt", "r", encoding='utf-8-sig')
prohos2pro = prohos2pro.read().split('\n')
province4 = ['ชัยนาท','พิจิตร','มหาสารคาม','ร้อยเอ็ด','สกลนคร','สระเเก้ว']
province3 = ['ชุมพร','ตาก','ปราจีนบุรี','พัทลุง','หนองบัวลำภู','อำนาจเจริญ']
province2 = ['บึงกาฬ','สตูล','สมุทรปราการ','สมุทรสงคราม','เพชรบุรี']
province1 = ['ตราด','นราธิวาส','ยะลา']
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
ansrich02 = 'ถ้าพร้อมเเล้ว มาลุยกันเล้ยยย!!\nミ●﹏☉'
ansrich03 = 'นี่ๆ อยากรู้อะไรบ้างเอ่ยเกี่ยวกับโรคซึมเศร้า ถามมาได้เลยน้าา ถ้ากอดอุ่นรู้ได้คำตอบเเน่นอน （´◔౪◔）'
ansrich04 = 'อยู่จังหวัดไหนเอ่ย ????? ۩۩۩۩'
ansrich05 = 'กอดอุ่นมีวิธีเบื้องต้นในการจัดการกับอารมณ์ เมื่อเกิดอาการซึมเศร้าลองทำตามดูน้าาา อาจการซึมเศร้าอาจจะน้อยลงก็ได้ ☺☻ '
ansrich06 = 'สามารถติดตามข่าวสารของโรคซึมเศร้าต่างๆ ได้ตามช่องทางข้างล่างนี้เลยน้าา ☜♥☞'
ans2 = ['มี','ไม่มี']
anss = ['ทำไรได้บ้าง','ทำไรได้','ทำไรได้บ้างอ่ะ','กอดอุ่นทำไรได้บ้างอ่ะ','เธอทำไรได้บ้างอ่ะ']
tess = 'สวัสดีจ้าา วันนี้มีอะไรอยากจะเม้าส์กับกอดอุ่นไหมเอ่ย?◑０◐\n เอ๊ะ!! หรือจะลองกดใช้งาน\nฟังก์ชันด้านล่างก็จิ้มที่ปุ่ม ">" สีเขียวได้เลยน้าา'
hos = 'ลองไปปรึกษากับกับจิตเเพทย์\nใกล้ๆบ้านดูน้าา'
game = 'พักสมองสักเเปบดีกว่าน้าา กอดอุ่นมีเกมส์มาให้เล่น สนใจไหม（´◔౪◔）'
anss01 = ['0.','1.','2.','3.']
app = Flask(__name__)

line_bot_api = LineBotApi('IzXs2WdxBaxjM/BTdVQ43pEYgt1O8BRRrEAOztjHPMfRUmM0BYtD4VRZg7MLMSyi1mWqI3vdPl08HfmsCUiBM1QJKc0OF89EfbEPIHEG+pKHO85//3Zvo+Qcf9MDZoFwe2m+cjasnyvwYZ3xPQNWPgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0dc428295a377a2e3ee1bda97af613e2')
# function for create tmp dir for download content###

            
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
Querich =' เอ๊ะๆ ดูเหมือนยังทำเเบบประเมิน\nไม่เสร็จเลย\nถ้าอยากทำต่ออันเดิม พิมพ์คำว่า\n"ทำต่อจากเดิม"\nเเต่ถ้าอยากเริ่มใหม่\nให้พิมพ์คำว่า "เริ่มทำใหม่"?'
re1 = "reg1"
re2 = "reg2"
re3 = "reg3"
re4 = "reg4"
re5 = "reg5"
re6 = "reg6"
re7 = "reg7"
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')


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
    regu1 = str(regular1(userid,question))
    regu2 = str(regular2(userid,question))
    regu3 = str(regular3(userid,question))
    #regu4 = str(regular4(userid,question))
    #regu5 = str(regular5(userid,question))
    regu6 = str(regular6(userid,question))
    regu7 = str(regular7(userid,question))
    #regu1 = "111"
    Qx = str(findxx(userid,question))
    print(Qx)
    Qy = str(findyy(userid,question))
    print(Qy)
    
    if regu1 == re1:
      answer = random.choice(evaluation_form['eval']['answer']) + ' เอ๊ะๆ วันนี้รู้สึกยังไงบ้างเอ่ย?'
      sticker_message = StickerSendMessage(
      package_id='2',
      sticker_id='22')
      line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
      line_bot_api.push_message(userid, sticker_message)
 
    elif regu2 == re2:
        answer = 'มีความรู้สึกเเบบนี้มานานถึงสองสัปดาห์ยังน้าา?\nพิมพ์คำว่า "ถึง" ถ้าเป็นมานานถึงสองสัปดาห์เเล้ว\nพิมพ์คำว่า "ยัง" ถ้ายังเป็นไม่ถึงสองสัปดาห์' 
        sticker_message = StickerSendMessage(
        package_id='2',
        sticker_id='149')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, sticker_message)
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=location_message))   
    elif regu3 == re3:
        answer = 'ฟังดูไม่มีอะไรน่าเป็นห่วงเนอะ อยากลองใช้ฟังก์ชันอย่างอื่นไหม พิมพ์คำว่า "ลอง" ถ้าอยากลอง พิมพ์คำว่า "ไม่ลอง" ถ้าไม่อยากลองทำ?'
        sticker_message = StickerSendMessage(
        package_id='2',
        sticker_id='172')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, sticker_message)
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=location_message)) 
    elif question== "ถึง":
        confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='✖✖ เอ๊ะ!!หยุดอ่านแป๊บนึงก่อนนะ\n▣เมื่อกดปุ่ม "เริ่มต้น"\n≡ตอบเเบบประเมิน 2 ข้อให้เสร็จ\n≡ก่อนที่จะทำอย่างอื่นนะจ๊ะ◡‿◡✿\n✎✎งั้นมาทำเเบบประเมินกันดีกว่า\nพร้อมยังจ๊ะ? ●０●\nพร้อมเเล้วกดเบาๆ ที่ปุ่มเลย▣◈',
                actions=[
                    MessageTemplateAction(
                        label='เริ่มทำ',
                        text='เริ่มทำ'
                    ),
                    MessageTemplateAction(
                        label='เพิ่มเติม',
                        text='เพิ่มเติม'
                    )
               ]
            )
        )
        #print("confirm_template_message")        
        #print(confirm_template_message)
        
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
        
    elif question == "ยัง": 
        answer = 'งั้นมาลองหาอะไรทำเพื่อผ่อนคลายกันเถอะเนอะ พิมพ์คำว่า "ลอง" ถ้าอยากลอง พิมพ์คำว่า "ไม่ลอง" ถ้าไม่อยากลองทำ'
        sticker_message = StickerSendMessage(
        package_id='3',
        sticker_id='218')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, sticker_message)
    elif question == "ลอง":
        confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
               text='ทำไรดีน้า ระหว่างฟังเพลงหรืออ่านิยายเพื่อผ่อนคลายดี?',
               actions=[
                    MessageTemplateAction(
                        label='ฟังเพลง',
                        text='ฟังเพลง'
                    ),
                    MessageTemplateAction(
                        label='อ่านนิยาย',
                        text='อ่านนิยาย'
                    )
               ]
            )
        )
        #print("confirm_template_message")        
        #print(confirm_template_message)
        
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
        
    elif question == "ไม่ลอง":
        answer = 'งั้นวันนี้กอดอุ่นต้องขอตัวไปก่อนนะ เเล้วไว้เจอกันใหม่ เมื่อคิดถึงกอดอุ่นเด้อออ'
        sticker_message = StickerSendMessage(
        package_id='2',
        sticker_id='158')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, sticker_message) 
        
    elif question == "ทำต่อจากเดิม": 
        Q9 = 0
        Q2 = 0
        Q9 = findxx(userid,question)
        print(Q9)
        Q2 = findyy(userid,question)
        print(Q2)
        db.delete_many({'No':findxx(userid,question)-1})
        answer = str(find1(userid,question))
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = answer,
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
    
                
    elif question == "เริ่มทำใหม่":
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
       
        
    elif question in 'อื่นๆ':
        answer = 'test'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
       
    elif question=="ฟังเพลง":
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                  CarouselColumn(
                      thumbnail_image_url='https://stickershop.line-scdn.net//stickershop/v1/product/1198016/iphone/main@2x.png',
                      title='เพลงผ่อนคลาย',
                      text='มาฟังเพลงกัน',
                      actions=[      
                          URITemplateAction(
                              label='ดนตรีสร้างสมาธิ',
                              uri='https://www.youtube.com/watch?v=KjkdT84wekA'
                          ), 
                          URITemplateAction(
                              label='สมองเเละความจำ',
                              uri='https://www.youtube.com/watch?v=H1l9EW8M1y4'
                          ),
                          URITemplateAction(
                              label='ดนตรีบำบัดความเครียด',
                              uri='https://www.youtube.com/watch?v=fBqXr7C1hQM&t=10s'
                           )
                        ]
                    ),
                    CarouselColumn(
                      thumbnail_image_url='https://i.pinimg.com/736x/90/de/ff/90deff63f4905e35d48d864f10982a04--line-sticker-the-smile.jpg',
                      title='ฟังเเล้วสดชื่น',
                      text='มาฟังกันเถอะ',
                      actions=[      
                          URITemplateAction(
                              label='วิธีใช้',
                              uri='https://www.youtube.com/watch?v=_ovBySUe4xM'
                          ), 
                          URITemplateAction(
                              label='ไม่ต้องให้คนทั้งโลก..',
                              uri='https://www.youtube.com/watch?v=NUZqlh7XLvg'
                          ),
                          URITemplateAction(
                              label='(เธอ Get ก็ OK)',
                              uri='https://www.youtube.com/watch?v=Sq-nfNrUoI8'
                           )
                        ]
                    ),
                    CarouselColumn(
                      thumbnail_image_url='https://image.dek-d.com/contentimg/2015/na/Nugirl/Beauty/76/Layer-1341.png',
                      title='ฟังเเล้วมั่น',
                      text='ฟังเเล้วมั่นใจในตัวเอง',
                      actions=[      
                          URITemplateAction(
                              label='All About..',
                              uri='https://www.youtube.com/watch?v=7PCkvCPvDXk'
                          ), 
                          URITemplateAction(
                              label='Beautiful..',
                              uri='https://www.youtube.com/watch?v=MrTz5xjmso4'
                          ),
                          URITemplateAction(
                              label='คนมีเสน่ห์',
                              uri='https://www.youtube.com/watch?v=R10mrTJpqPw'
                           )
                        ]
                    )    
                 ]
              )
          )
        line_bot_api.reply_message(event.reply_token,  carousel_template_message) 
        
    elif question in 'อ่านนิยาย':
        carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                  CarouselColumn(
                      thumbnail_image_url='https://image.dek-d.com/contentimg/2014/nong/BG%26Icon/read05.png',
                      title='นิยายรักสดใส',
                      text='มาอ่านกันเถอะ',
                      actions=[      
                          URITemplateAction(
                              label='เสน่ห์ดลใจรัก',
                              uri='https://writer.dek-d.com/sea-bing/story/view.php?id=1802727'
                          ), 
                          URITemplateAction(
                              label='ฤดูสดใสให้หัวใจมีรัก',
                              uri='https://writer.dek-d.com/jee12/story/view.php?id=788257'
                          ),
                          URITemplateAction(
                              label='ฉลามอย่าโกรธ',
                              uri='https://writer.dek-d.com/gamsang2/story/view.php?id=1826327'
                           )
                        ]
                    ),
                    CarouselColumn(
                      thumbnail_image_url='https://supatra89.files.wordpress.com/2011/09/106368-attachment.jpg',
                      title='นิยายเเฟนตาซี',
                      text='มาอ่านกันเถอะ',
                      actions=[      
                          URITemplateAction(
                              label='นักปราบผีแห่ง..',
                              uri='https://fictionlog.co/b/592e7a13b0dad878b4ce0fe7'
                          ), 
                          URITemplateAction(
                              label='ระบบเปลี่ยนชีวิต',
                              uri='https://fictionlog.co/b/5aefd40e9e33a33c0d88c893'
                          ),
                          URITemplateAction(
                              label='อสูรพิทักษ์ข้ามภพ',
                              uri='https://fictionlog.co/b/5a8c3b5d7497096a599d61e6'
                           )
                        ]
                    ),
                    CarouselColumn(
                      thumbnail_image_url='https://areatablet.files.wordpress.com/2011/03/imagesca5kb6mc.jpg',
                      title='อ่านเเล้วอ่านอีก',
                      text='มาอ่านกันเถอะ',
                      actions=[      
                          URITemplateAction(
                              label='ต้องลดให้ได้ 5..',
                              uri='https://www.webtoons.com/th/drama/demi-5kg/list?title_no=1157'
                          ), 
                          URITemplateAction(
                              label='สาวน้อยร้อยช่าง',
                              uri='https://www.webtoons.com/th/tiptoon/the-diy-girl/list?title_no=737&page=4'
                          ),
                          URITemplateAction(
                              label='ครัวง่ายๆสไตล์..',
                              uri='https://www.webtoons.com/th/tiptoon/lazy-cooking/list?title_no=646'
                           )
                        ]
                    )
                 ]
              )
          )
        line_bot_api.reply_message(event.reply_token,  carousel_template_message) 
      
        
    elif question == richmanu['rich']['rich01']:
        answer = ansrich01
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        #################################ส่วนนี้เด่วทำทีหลังสุด####################################################
    elif question == richmanu['rich']['rich02']:
        #answer = ansrich02
        if Qy=="0":
             print(Qy)
             answer = random.choice(evaluation_form['eval']['answer']) + ' เอ๊ะๆ วันนี้รู้สึกยังไงบ้างเอ่ย?'
             sticker_message = StickerSendMessage(
             package_id='2',
             sticker_id='22')
             line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
             line_bot_api.push_message(userid, sticker_message)
        else:
             answer = random.choice(evaluation_form['eval']['answer']) + Querich 
             sticker_message = StickerSendMessage(
             package_id='2',
             sticker_id='24')
             line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
             line_bot_api.push_message(userid, sticker_message)
             #answer = random.choice(evaluation_form['eval']['answer']) + ' เอ๊ะๆ วันนี้รู้สึกยังไงบ้างเอ่ย?'
             #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
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
                        #thumbnail_image_url='https://s.isanook.com/he/0/ud/1/9229/sad.jpg',
                        thumbnail_image_url = 'https://i.imgur.com/j6c4KEp.jpg',
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
    
    elif regu7 == re7:
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
                        label='เมนูหลัก',
                        text='เมนูหลัก'
                    )
                ]
             )
          )
        
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif question == "เมนูหลัก":
        #question1 = str(find1(userid,question))
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=question1))
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='กอดอุ่นทำได้ๆ',
                text='ลองเลือกใช้ดูหน่อยนะจ๊ะ',
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
                        label='จิตเวชใกล้',
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
    
    elif question == "สรุปแบบประเมิน":
        answer = str(scoreC(userid,question))
        image_message = ImageSendMessage(
        original_content_url=scorephoto(userid,question),
        preview_image_url=scorephoto(userid,question)
        )
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, image_message)  
   
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
    elif question in lo:
       kk = str(scoreme2)
       if kk=="ไม่ปกติ":
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
          line_bot_api.reply_message(event.reply_token, confirm_template_message)
       else:
          confirm_template_message = TemplateSendMessage(
              alt_text='Confirm template',
              template=ConfirmTemplate(
                  text="อาการดูไม่มีอะไรผิดปกติเนอะ เเต่เอ๊ะ! เมื่อกี้ตั้งใจตอบหรือเปล่าน้าาา ถ้าไม่ได้ตั้งใจลองกลับไปเริ่มใหม่สิ เเต่ถ้าตั้งใจเเล้ว ฟังเพลง คลายเครียดกัน",
                  actions=[
                      MessageTemplateAction(
                          label='เริ่มทำใหม่',
                           text='เริ่มทำใหม่'
                      ),
                      MessageTemplateAction(
                          label='ฟังเพลง',
                          text='ฟังเพลง'
                      )
                  ]
              )
          )
          line_bot_api.reply_message(event.reply_token, confirm_template_message)
        #print("confirm_template_message")        
        #print(confirm_template_message)
        
        
  
    elif question in 't':
        confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
               text=str(find3(userid,question)),
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
      
    elif question in 'a':
        confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
               text=str(findx(userid,question)),
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
        
    elif question in 'b':
        confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
               text=str(findy(userid,question)),
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
        
    elif question in 'c':
        confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
               text=str(findxy(userid,question)),
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
      
    elif question == "สนใจ":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/A7dJsdh.jpg',
                title='นาฬิกาเรือนไหนของจริง',
                text='เลือกสิๆ',
                actions=[
                    MessageTemplateAction(
                        label='A',
                        text='A',
                    ),
                    MessageTemplateAction(
                        label='B',
                        text='B'
                    )
                ]
             )
          )
        
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        
    elif question == "A":
        answer = 'ถูกต้องจ้าาาาาา ⊙０⊙'+'\n'+'เฉลย เรือน "A" จ้า เพราะถ้าเกิดนาฬิกาเดินเข็มวินาทีจะชนจ้าาา'+'\n'+'ถ้าจะทำต่อพิมพ์คำว่า "ทำต่อ"'+'\n'+'ถ้าอยากใช้ฟังก์ชันก์ใหม่ ให้พิมพ์ "ฟังก์ชันเพิ่มเติม" นะจ๊ะ'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    
    elif question == "B":
        answer = 'ผิดจ้าาาาาา ⊙﹏⊙'+'\n'+'เฉลย เรือน "A" จ้า เพราะถ้าเกิดนาฬิกาเดินเข็มวินาทีจะชนจ้าาา'+'\n'+'ถ้าจะทำต่อพิมพ์คำว่า "ทำต่อ"'+'\n'+'ถ้าอยากใช้ฟังก์ชันก์ใหม่ ให้พิมพ์ "ฟังก์ชันเพิ่มเติม" นะจ๊ะ'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
    
    elif question in happy:
        answer = 'ฟังดูไม่น่าเป็นห่วงเท่าไหร่เนอะ กอดอุ่นมีเพลงกับนิยายมาเเนะนำลองฟังดูป่ะ'
        sticker_message = StickerSendMessage(
        package_id='1',
        sticker_id='125')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, sticker_message)
        
    elif regu6 == re6:
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'สะดวกไหนเลือกเลยนะจ๊ะ',
                text='พบผู้เชี่ยวชาญใกล้บ้านกันเถอะ',
                actions=[
                    MessageTemplateAction(
                        label='รพ.จุฬาลงกรณ์',
                        text='โรงพยาบาลจุฬาลงกรณ์',
                    ),
                    MessageTemplateAction(
                        label='รพ.ศิริราช',
                        text='โรงพยาบาลศิริราช'
                    ),
                    MessageTemplateAction(
                        label='รพ.รามาธิบดี',
                        text='โรงพยาบาลรามาธิบดี'
                    ),
                    MessageTemplateAction(
                        label='ดูโรงพยาบาลต่อ',
                        text='ดูโรงพยาบาลต่อ'
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        
    elif question == "ดูโรงพยาบาลต่อ":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'สะดวกไหนเลือกเลยนะจ๊ะ',
                text='พบผู้เชี่ยวชาญใกล้บ้านกันเถอะ',
                actions=[
                    MessageTemplateAction(
                        label='รพ.ภูมิพลอดุลยเดช',
                        text='โรงพยาบาลภูมิพลอดุลยเดช',
                    ),
                    MessageTemplateAction(
                        label='รพ.วชิรพยาบาล',
                        text='โรงพยาบาลวชิรพยาบาล'
                    ),
                    MessageTemplateAction(
                        label='ก่อนหน้า',
                        text='ก่อนหน้า'
                    ),
                    MessageTemplateAction(
                        label='ดูถัดไป',
                        text='ดูถัดไป'
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif question == "ก่อนหน้า":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'สะดวกไหนเลือกเลยนะจ๊ะ',
                text='พบผู้เชี่ยวชาญใกล้บ้านกันเถอะ',
                actions=[
                    MessageTemplateAction(
                        label='รพ.จุฬาลงกรณ์',
                        text='โรงพยาบาลจุฬาลงกรณ์',
                    ),
                    MessageTemplateAction(
                        label='รพ.ศิริราช',
                        text='โรงพยาบาลศิริราช'
                    ),
                    MessageTemplateAction(
                        label='รพ.รามาธิบดี',
                        text='โรงพยาบาลรามาธิบดี'
                    ),
                    MessageTemplateAction(
                        label='ดูโรงพยาบาลต่อ',
                        text='ดูโรงพยาบาลต่อ'
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    
    elif question == "ดูถัดไป":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'สะดวกไหนเลือกเลยนะจ๊ะ',
                text='พบผู้เชี่ยวชาญใกล้บ้านกันเถอะ',
                actions=[
                    MessageTemplateAction(
                        label='สถาบันราชานุกูล',
                        text='สถาบันราชานุกูล',
                    ),
                    MessageTemplateAction(
                        label='สถาบันสุขภาพจิตเด็ก',
                        text='สถาบันสุขภาพจิตเด็กและวัยรุ่นราชนครินทร์'
                    ),
                    MessageTemplateAction(
                        label='ก่อนหน้า',
                        text='ก่อนหน้า.'
                    ),
                    MessageTemplateAction(
                        label='ดูถัดไป',
                        text='ดูถัดไป.'
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        
    elif question == "ก่อนหน้า.":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'สะดวกไหนเลือกเลยนะจ๊ะ',
                text='พบผู้เชี่ยวชาญใกล้บ้านกันเถอะ',
                actions=[
                    MessageTemplateAction(
                        label='รพ.ภูมิพลอดุลยเดช',
                        text='โรงพยาบาลภูมิพลอดุลยเดช',
                    ),
                    MessageTemplateAction(
                        label='รพ.วชิรพยาบาล',
                        text='โรงพยาบาลวชิรพยาบาล'
                    ),
                    MessageTemplateAction(
                        label='ก่อนหน้า',
                        text='ก่อนหน้า'
                    ),
                    MessageTemplateAction(
                        label='ดูถัดไป',
                        text='ดูถัดไป'
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    
    elif question == "ดูถัดไป.":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'สะดวกไหนเลือกเลยนะจ๊ะ',
                text='พบผู้เชี่ยวชาญใกล้บ้านกันเถอะ',
                actions=[
                    MessageTemplateAction(
                        label='สถาบันสุขภาพเด็ก',
                        text='สถาบันสุขภาพเด็กแห่งชาติมหาราชินี (โรงพยาบาลเด็ก)',
                    ),
                    MessageTemplateAction(
                        label='รพ.ตำรวจ',
                        text='โรงพยาบาลตำรวจ'
                    ),
                    MessageTemplateAction(
                        label='ดูก่อนหน้า',
                        text='ดูก่อนหน้า.'
                    ),
                    MessageTemplateAction(
                        label='ดูโรงพยาบาลต่อ',
                        text='ดูโรงพยาบาลต่อ.'
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)   
        
    elif question == "ดูก่อนหน้า.":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'สะดวกไหนเลือกเลยนะจ๊ะ',
                text='พบผู้เชี่ยวชาญใกล้บ้านกันเถอะ',
                actions=[
                    MessageTemplateAction(
                        label='สถาบันราชานุกูล',
                        text='สถาบันราชานุกูล',
                    ),
                    MessageTemplateAction(
                        label='สถาบันสุขภาพจิตเด็ก',
                        text='สถาบันสุขภาพจิตเด็กและวัยรุ่นราชนครินทร์'
                    ),
                    MessageTemplateAction(
                        label='ก่อนหน้า',
                        text='ก่อนหน้า.'
                    ),
                    MessageTemplateAction(
                        label='ดูถัดไป',
                        text='ดูถัดไป.'
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        
    elif question == "ดูโรงพยาบาลต่อ.":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'สะดวกไหนเลือกเลยนะจ๊ะ',
                text='พบผู้เชี่ยวชาญใกล้บ้านกันเถอะ',
                actions=[
                    MessageTemplateAction(
                        label='รพ.ทหารผ่านศึก',
                        text='โรงพยาบาลทหารผ่านศึก',
                    ),
                    MessageTemplateAction(
                        label='รพ.พระมงกุฎเกล้า',
                        text='โรงพยาบาลพระมงกุฎเกล้า'
                    ),
                    MessageTemplateAction(
                        label='กลับไปหน้าก่อนหน้า',
                        text='กลับไปหน้าก่อนหน้า'
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        
    elif question == "กลับไปหน้าก่อนหน้า":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'สะดวกไหนเลือกเลยนะจ๊ะ',
                text='พบผู้เชี่ยวชาญใกล้บ้านกันเถอะ',
                actions=[
                    MessageTemplateAction(
                        label='สถาบันสุขภาพเด็ก',
                        text='สถาบันสุขภาพเด็กแห่งชาติมหาราชินี (โรงพยาบาลเด็ก)',
                    ),
                    MessageTemplateAction(
                        label='รพ.ตำรวจ',
                        text='โรงพยาบาลตำรวจ'
                    ),
                    MessageTemplateAction(
                        label='ดูก่อนหน้า',
                        text='ดูก่อนหน้า.'
                    ),
                    MessageTemplateAction(
                        label='ดูโรงพยาบาลต่อ',
                        text='ดูโรงพยาบาลต่อ.'
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)   
        
        
    elif question == "ขอนเเก่น":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'สะดวกไหนเลือกเลยนะจ๊ะ',
                text='พบผู้เชี่ยวชาญใกล้บ้านกันเถอะ',
                actions=[
                    MessageTemplateAction(
                        label='รพ.ศรีนครินทร์',
                        text='โรงพยาบาลศรีนครินทร์ คณะแพทยศาสตร์ มหาวิทยาลัยขอนแก่น',
                    ),
                    MessageTemplateAction(
                        label='รพ.ศูนย์ขอนแก่น',
                        text='โรงพยาบาลศูนย์ขอนแก่น'
                    ),
                    MessageTemplateAction(
                        label='สถาบันพัฒนาการเด็ก',
                        text='สถาบันพัฒนาการเด็กภาคตะวันออกเฉียงเหนือ'
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)   
    
    elif question in prohos2pro:
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'สะดวกไหนเลือกเลยนะจ๊ะ',
                text='พบผู้เชี่ยวชาญใกล้บ้านกันเถอะ',
                actions=[
                    MessageTemplateAction(
                        label = "รพ."+str(tud21(question)),
                        text = str(hospro1(question))
                    ),
                    MessageTemplateAction(
                        label = "รพ."+str(tud22(question)),
                        text = str(hospro2(question))
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        
    elif question in NameHospital:
        answer = hos+'\n'+str(addressProhos(question))
        location_message = LocationSendMessage(
        title = provinceehos(question),
        address = hospiName(question),
        latitude = namehosLati(question),
        longitude = namehosLong(question) )
        sticker_message = StickerSendMessage(
        package_id='2',
        sticker_id='176')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, location_message)
        line_bot_api.push_message(userid, sticker_message)
    #################### แผนที่ที่เหลือ ####################################################    
    elif question in province4:
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'ไม่มีสถานบริการด้านจิตเวช',
                text='เลือกจังหวัดอื่นที่ใกล้บ้าน',
                actions=[
                    MessageTemplateAction(
                        label= provincenot4(question,0),
                        text= provincenot4(question,0)
                    ),
                    MessageTemplateAction(
                        label= provincenot4(question,1),
                        text= provincenot4(question,1)
                    ),
                    MessageTemplateAction(
                        label= provincenot4(question,2),
                        text = provincenot4(question,2)
                    ),
                    MessageTemplateAction(
                        label= provincenot4(question,3),
                        text= provincenot4(question,3)
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        
    elif question in province3:
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'ไม่มีสถานบริการด้านจิตเวช',
                text='เลือกจังหวัดอื่นที่ใกล้บ้าน',
                actions=[
                    MessageTemplateAction(
                        label= provincenot3(question,0),
                        text= provincenot3(question,0)
                    ),
                    MessageTemplateAction(
                        label= provincenot3(question,1),
                        text= provincenot3(question,1)
                    ),
                    MessageTemplateAction(
                        label= provincenot3(question,2),
                        text = provincenot3(question,2)
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        
    elif question in province2:
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'ไม่มีสถานบริการด้านจิตเวช',
                text='เลือกจังหวัดอื่นที่ใกล้บ้าน',
                actions=[
                    MessageTemplateAction(
                        label= provincenot2(question,0),
                        text= provincenot2(question,0)
                    ),
                    MessageTemplateAction(
                        label= provincenot2(question,1),
                        text= provincenot2(question,1)
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)    
        
    elif question in province1:
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title = 'ไม่มีสถานบริการด้านจิตเวช',
                text='เลือกจังหวัดอื่นที่ใกล้บ้าน',
                actions=[
                    MessageTemplateAction(
                        label= provincenot1(question,0),
                        text= provincenot1(question,0)
                    )
                ]
             )
          )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)   
        
    elif question =="ขิมเหนื่อย":
        answer = "test"
        image_message = ImageSendMessage(
        original_content_url=scorephoto(userid,question),
        preview_image_url=scorephoto(userid,question)
        )
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, image_message)  
        
        
        
        
             
    else:
        answer = listQNo 
        #userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        sticker_message = StickerSendMessage(
        package_id='2',
        sticker_id='30')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        line_bot_api.push_message(userid, sticker_message)
 
@mock_s3
@handler.add(MessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
def handle_content_message(event):
   userid = event.source.user_id
   #path = "https://s3-ap-southeast-1.amazonaws.com/khim/"
   #os.listdir(path)
   ACCESS_KEY_ID = 'AKIAID3EAOJCS2LXRQ2A'
   SECRET_ACCESS_KEY ='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'
   REGION_NAME = 'us-east-1'
   
   session = Session(
       aws_access_key_id=ACCESS_KEY_ID,
       aws_secret_access_key=SECRET_ACCESS_KEY
   )
   s3 = session.resource("s3")
   s3.create_bucket(Bucket='khim', ACL='public-read', CreateBucketConfiguration={
    'LocationConstraint': REGION_NAME})
   BUCKET_NAME = 'khim'
   s3 = session.client("s3")
   filename = 'NameHospital.txt'
   s3.upload_file(filename, BUCKET_NAME, "เหงา.wav")


   if isinstance(event.message, ImageMessage):
       ext = 'jpg'
   elif isinstance(event.message, VideoMessage):
       ext = 'mp4'
   elif isinstance(event.message, AudioMessage):
       ext = 'm4a'
   else:
       return

   message_content = line_bot_api.get_message_content(event.message.id)
   print("-------------------------")
   print(message_content)
   print("-------------------------")
   print(event.message.id)
   print("-------------------------")
   print(ext)
   with tempfile.NamedTemporaryFile(prefix=userid + '-', delete=False) as tt:
       for chunk in message_content.iter_content():
           #print(chunk)
           tt.write(chunk)
           file = tt.name
       file_path = file  + '.' + ext
   dist_name = os.path.basename(file_path)
   os.stat(file)
   os.rename(file, file_path)
   print(".......................")
   print(".....................up")
   client = boto3.client('s3')
   print(".....................upload")
   print(dist_name)
   print(file_path)
   print(file)
   #client.upload_file(Bucket=BUCKET_NAME, Key='test.wav', Filename=file_path)
   #client.upload_file(file_path, '/'.join([BUCKET_NAME,'k.wav']), Key= file_path)
   #file
   client = boto3.client("s3")
   client.upload_file(Bucket=BUCKET_NAME, Key='test.wav', Filename=file_path, Config=TransferConfig(use_threads=False))
   #s3.Bucket(BUCKET_NAME).put_object(Key='test.wav', Body=data)
   line_bot_api.reply_message(event.reply_token, TextSendMessage(text="ooooo"))
    
    #dist_name = os.path.basename(dist_path)
    #os.rename(tempfile_path, dist_path)

    #line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='Save content.'),
            #TextSendMessage(text=request.host_url + os.path.join('static', 'tmp', dist_name))
        #])
    
    
 



        

if __name__ == "__main__":
    app.run()
