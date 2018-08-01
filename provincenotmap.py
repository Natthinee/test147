# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 00:07:40 2018

@author: Natthinee
"""
province1 = ['อุทัยธานี','สิงห์บุรี','นครสวรรค์','สุพรรณบุรี'] 
province2 = ['พิษณุโลก','เพชรบูรณ์','นครสวรรค์','กำแพงเพชร']
province3 = ['ขอนแก่น','กาฬสินธุ์','บุรีรัมย์','สุรินทร์']
province4 = ['กาฬสินธุ์','มุกดาหาร','ยโสธร','ศรีสะเกษ']
province5 = ['หนองคาย','มุกดาหาร','กาฬสินธุ์','อุดรธานี']
province6 = ['จันทบุรี','ฉะเชิงเทรา','นครราชสีมา','บุรีรัมย์']

province11 = ['ประจวบคีรีขันธ์','สุราษฎร์ธานี','ระนอง']
province12 = ['แม่ฮ่องสอน','สุโขทัย','กาญจนบุรี']
province13 = ['นครนายก','นครราชสีมา','ฉะเชิงเทรา']
province14 = ['นครศรีธรรมราช','สงขลา','ตรัง']
province15 = ['อุดรธานี','ขอนแก่น','เลย']
province16 = ['มุกดาหาร','ยโสธร','อุบลราชธานี']

province21 = ['หนองคาย','นครพนม']
province22 = ['ตรัง','สงขลา']
province23 = ['กรุงเทพ','ฉะเชิงเทรา']
province24 = ['สมุทรสาคร','ราชบุรี']
province25 = ['ราชบุรี','จังหวัดประจวบคีรีขันธ์']

province01 = ['จันทบุรี']
province02 = ['ปัตตานี']
province03 = ['ปัตตานี']


def provincenot4(question,number):
    if question == "ชัยนาท":
        return province1[number]
    
    elif question == "พิจิตร":
        return province2[number]
    
    elif question == "มหาสารคาม":
        return province3[number]
    
    elif question == "ร้อยเอ็ด":
        return province4[number]
    
    elif question == "สกลนคร":
        return province5[number]  
    
    elif question == "สระเเก้ว":
        return province6[number] 
    
def provincenot3(question,number):
    if question == "ชุมพร":
        return province11[number]
    
    elif question == "ตาก":
        return province12[number]
    
    elif question == "ปราจีนบุรี":
        return province13[number]
    
    elif question == "พัทลุง":
        return province14[number]
    
    elif question == "หนองบัวลำภู":
        return province15[number]
    
    elif question == "อำนาจเจริญ":
        return province16[number]
    
def provincenot2(question,number):
    if question == "บึงกาฬ":
        return province21[number]
    
    elif question == "สตูล":
        return province22[number]
    
    elif question == "สมุทรปราการ":
        return province23[number]
    
    elif question == "สมุทรสงคราม":
        return province24[number]
    
    elif question == "เพชรบุรี":
        return province25[number]
    
def provincenot1(question,number):
    if question == "ตราด":
        return province01[number]
    
    elif question == "นราธิวาส":
        return province02[number]
    
    elif question == "ยะลา":
        return province03[number]
    
    
    
    
    
    
    
    
    
    
    
    
    