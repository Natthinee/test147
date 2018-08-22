
# coding: utf-8

# In[2]:


import os
import numpy as np
#import keras
import cntk
from scipy.io import wavfile
import requests
# from ftplib import FTP
# ftp = FTP('nonggodaun.plearnjai.com')
# ftp.login(user='nonggodaun@plearnjai.com', passwd = 'Q6YLnl5CL')

# keras.models.load_model(filepath)


# In[3]:


#cntk.try_set_default_device( cntk.all_devices()[0] )


# In[4]:


def evalualte_Multilayer(file_path, sec=1):
    
    rate, audio = wavfile.read( file_path )
    rate*=sec
#     #audio = np.mean(audio, axis=1)
    audio = np.trim_zeros(audio)
    audio = audio[:len(audio)-(len(audio)%rate)]
    rates = [ audio[i:i+rate] for i in range( 0, len(audio), rate ) ]

    x_test = np.asarray( [rate for rate in rates], dtype=np.float32 )
    x_test = np.tanh( x_test )

    label = 1
    if "ปกติ" in file_path:
        label = 0
    results = model.predict( x_test )
    count_label = 0
    for result in results:
        i = np.argmax(result)
        if i == label:
            count_label += 1
        
    count_wrong = len( x_test ) - count_label
    
    if count_wrong > count_label:
        return "ปกติ"
    if count_wrong == count_label:
        return "ปกติ"
    return "เศร้า"


# # In[5]:


def evalualte_CNN_1D(file_path, sec=1):
    print( "FILE: %s => " % file_path , end="" )
    rate, audio = wavfile.read( file_path )
    rate*=sec
#     #audio = np.mean(audio, axis=1)
    audio = np.trim_zeros(audio)
    audio = audio[:len(audio)-(len(audio)%rate)]
    rates = [ audio[i:i+rate] for i in range( 0, len(audio), rate ) ]

    x_test = np.asarray( [rate for rate in rates], dtype=np.float32 )
    x_test = np.tanh(x_test)
    x_test = x_test.reshape( x_test.shape[0], x_test.shape[1], 1 )
    label = 1
    if "ปกติ" in file_path:
        label = 0
    results = model.predict( x_test )
    count_label = 0
    for result in results:
        i = np.argmax(result)
        if i == label:
            count_label += 1
        
    count_wrong = len( x_test ) - count_label
    if count_wrong > count_label:
        return "ปกติ"
    if count_wrong == count_label:
        return "ปกติ"
    return "เศร้า"


# # In[6]:


def evalualte_CNN_2D(file_path, sec=1):
    print( "FILE: %s => " % file_path , end="" )
    rate, audio = wavfile.read( file_path )
    rate*=sec
#     #audio = np.mean(audio, axis=1)
    audio = np.trim_zeros(audio)
    audio = audio[:len(audio)-(len(audio)%rate)]
    rates = [ audio[i:i+rate] for i in range( 0, len(audio), rate ) ]
    
    

    x_test = np.asarray( [np.resize( np.asarray( frame ), (img_rows, img_cols) ) for frame in rates], dtype=np.float32 )
    x_test = ( x_test - np.min(x_train2) ) / ( np.max(x_train2) - np.min(x_train2) )
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    
    
    label = 1
    if "ปกติ" in file_path:
        label = 0
    results = model.predict( x_test )
    count_label = 0
    for result in results:
        i = np.argmax(result)
        if i == label:
            count_label += 1
        
    count_wrong = len( x_test ) - count_label
    if count_wrong > count_label:
        return "ปกติ"
    if count_wrong == count_label:
        return "ปกติ"
    return "เศร้า"


# # In[7]:

# # from keras.utils.data_utils import get_file
# # model_path = get_file(
# #             'Model_0001.h5',
# #             'https://nonggodaun.plearnjai.com/ffmpeg-4.0.2/Model_0001.h5')
# # import pandas as pd
# # url = 'http://192.168.1.81:50070/stocks/test/pred/20140103/000001.h5'
# # df = pd.read_hdf(url)
# #model_folder = os.path.join( os.getcwd(), "Model" )

# # model_name = "Model_0001.h5"
# # model = keras.models.load_model(model_name)
# # #print( model.input_shape )
# # #model.summary()


# # In[10]:



# # sec = 3
# # img_rows = 28
# # img_cols = 28
# # input_shape = (img_rows, img_cols, 1)

# # file_folder = os.path.join( os.getcwd() , "WAV_files" )
# # file_path = os.path.join( file_folder, "ปกติ01.wav" )
# # path = file_path

# # print( "FILE: %s => " % path, end="" )
# # # ------------------------------------
# # ans = evalualte_Multilayer(path, sec)
# # # ans = evalualte_CNN_1D(path, sec)
# # # ans = evalualte_CNN_2D(path, sec)
# # # ------------------------------------
# # print(ans)


# # In[ ]:


# # def result(file,userid):
# #     sec = 3
# #     img_rows = 28
# #     img_cols = 28
# #     input_shape = (img_rows, img_cols, 1)

# #     file_folder = os.path.join( os.getcwd() , "WAV_files" )
# #     file_path = os.path.join( file_folder, "ปกติ01.wav" )
# #     path = file_path

# #     print( "FILE: %s => " % path, end="" )
# # # ------------------------------------
# #     ans = evalualte_Multilayer(path, sec)
# # # ans = evalualte_CNN_1D(path, sec)
# # # ans = evalualte_CNN_2D(path, sec)
# # # ------------------------------------
# #     print(ans)
# #     return ans


# # In[ ]:

def result(userid,file):
    print("test")
    url ='http://nonggodaun.plearnjai.com/Model_0001.h5'
    r = requests.get(url)
    with open('Model_0001.h5', 'wb') as f:  
        k = f.write(r.content)
    model_name = 'Model_0001.h5'
    model = keras.models.load_model(model_name)
    #print( model.input_shape )
    #model.summary()
    
    url = 'http://nonggodaun.plearnjai.com/'+file
    #print (url)
    r = requests.get(url)
    with open('kim.m4a', 'wb') as f:  
        k = f.write(r.content)

    if os.path.exists('tmp.wav'):
        os.remove( 'tmp.wav' )
   
    os.system( "ffmpeg -i kim.m4a -ar 44100 tmp.wav" )
    sec = 3
    img_rows = 28
    img_cols = 28
    input_shape = (img_rows, img_cols, 1)
    path = 'tmp.wav'
    print( "FILE: %s => " % path, end="" )
# ------------------------------------
    ans = evalualte_Multilayer(path, sec)
# ans = evalualte_CNN_1D(path, sec)
# ans = evalualte_CNN_2D(path, sec)
# ------------------------------------
    #ftp.delete(file)
    return ans

