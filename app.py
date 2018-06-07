from flask import Flask, request
import json
import requests
import random
listanswer = []
question = ''
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
setscoreq9['score'] = {'pprint': '0 = ไม่มีเลย\n 1 = เป็นบางวัน\n 2 = เป็นบ่อย\n 3 = เป็นทุกวัน\n'}
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

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
# ห้ามลบคำว่า Bearer ออกนะครับเมื่อนำ access token มาใส่
LINE_API_KEY = 'Bearer IzXs2WdxBaxjM/BTdVQ43pEYgt1O8BRRrEAOztjHPMfRUmM0BYtD4VRZg7MLMSyi1mWqI3vdPl08HfmsCUiBM1QJKc0OF89EfbEPIHEG+pKHO85//3Zvo+Qcf9MDZoFwe2m+cjasnyvwYZ3xPQNWPgdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)


@app.route('/')
def index():
    return 'สวัสดีชาวโลก.'


@app.route('/bot', methods=['POST'])
def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyQueue = list()

    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)

    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']

    # ส่วนนี้ดึงข้อมูลพื้นฐานออกมาจาก json (เผื่อ)
    userID = msg_in_json["events"][0]['source']['userId']
    msgType = msg_in_json["events"][0]['message']['type']

    # ตรวจสอบว่า ที่ส่งเข้ามาเป็น text รึป่าว (อาจเป็น รูป, location อะไรแบบนี้ได้ครับ)
    # แต่ก็สามารถประมวลผลข้อมูลประเภทอื่นได้นะครับ
    # เช่น ถ้าส่งมาเป็น location ทำการดึง lat long ออกมาทำบางอย่าง เป็นต้น
    #if msgType != 'text':
        #reply(replyToken, ['Only text is allowed.'])
        #return 'OK', 200

    # ตรงนี้ต้องแน่ใจว่า msgType เป็นประเภท text ถึงเรียกได้ครับ
    # lower เพื่อให้เป็นตัวพิมพ์เล็ก strip เพื่อนำช่องว่างหัวท้ายออก ครับ
    text = msg_in_json["events"][0]['message']['text'].lower().strip()

    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ exact match
    
    if text in evaluation_form['eval']['greet'] :
         replyQueue.append(random.choice(evaluation_form['eval']['answer'] ))
         reply2(replyToken, replyQueue[:5])
         return 'OK',200
    elif text in evaluation_form['eval']['ques']  :
         question = random.choice(evaluation_form['eval']['quest9'])
         face = random.choice(evaluation_form['eval']['wordap'])
         listanswer.append(question)
         replyQueue.append(face+question)
         replyQueue.append(setscoreq9['score']['pprint'])
         replyQueue.append(please['ple']['ple'])
         reply(replyToken, replyQueue[:5])
         return 'OK',200
    else:
         with open("tes.txt","a",encoding="utf8") as f:
             f.write('khim')
         replyQueue.append('งง')
         reply3(replyToken, replyQueue[:5])
         return 'OK', 200


    # ตอบข้อความ "นี่คือรูปแบบข้อความที่รับส่ง" กลับไป
    #replyQueue.append(text)


    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    #replyQueue.append(msg_in_string)
  
  


def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type": "text",
            "text": text
        })
    data = json.dumps({
        "replyToken": replyToken,
        "messages": msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return
def reply1(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
             "type": "sticker",
             "packageId": "1",
             "stickerId": "4"
        })
    data = json.dumps({
        "replyToken": replyToken,
        "messages": msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return
def reply2(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
             "type": "template",
             "altText": "this is a confirm template",
             "template": {
                 "type": "buttons",
                 "text": random.choice(evaluation_form['eval']['quest9']),
                 "actions": [
                     {
                       "type": "message",
                       "label": "ไม่มีเลย",
                       "text": "ไม่มีเลย"
                     },
                     {
                       "type": "message",
                       "label": "เป็นบางวัน",
                       "text": "เป็นบางวัน"
                     },
                     {
                       "type": "message",
                       "label": "เป็นบ่อย",
                       "text": "เป็นบ่อย"
                     },
                     {
                       "type": "message",
                       "label": "เป็นทุกวัน",
                       "text": "เป็นทุกวัน"
                     }
                 ]
           }


        })
    data = json.dumps({
        "replyToken": replyToken,
        "messages": msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return
def reply3(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/{messageId}/content'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
             "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
             "type": "message",
             "timestamp": 1462629479859,
             "source": {
               "type": "user",
               "userId": "U4af4980629..."
             },
             "message": {
               "id": "325708",
               "type": "audio"
             }

        })
    data = json.dumps({
        "replyToken": replyToken,
        "messages": msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return
  
  
 
if __name__ == '__main__':
    app.run()
