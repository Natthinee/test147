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
                   'rich05': 'เศร้าเเล้วเปลี่ยน',
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
        userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        
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
                        title='ปรับสติสร้างสมาธิ',
                        text='มาเริ่มสร้างสมาธิให้จิตใจ',
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
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://png.pngtree.com/element_origin_min_pic/00/09/45/3656a089293a620.jpg',
                        title='ออกกำลังกายสร้างกำลังใจ',
                        text='ขยับวันละนิดปรับเปลี่ยนชีวิตสดใส',
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
    else:
        answer = listQNo 
        #userr.insert({"UserID":userid,"Question": question, "Answer": answer})
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=answer))
        


if __name__ == "__main__":
    app.run()
