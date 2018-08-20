# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 17:18:41 2018

@author: Natthinee
"""

import os

import cntk
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

from scipy.io import wavfile
import numpy as np
from random import shuffle
import math
sec = 3

root, _dirs, files = next(os.walk( os.path.join( os.getcwd(), os.path.join( "dataset", "train" ))))
train_paths = [ os.path.join( root, file ) for file in files ]

root, _dirs, files = next(os.walk( os.path.join( os.getcwd(), os.path.join( "dataset", "test" ))))
test_paths = [ os.path.join( root, file ) for file in files ]

def create_samples(file_path, sec=1):
    rate, audio = wavfile.read( file_path )
    rate *= sec
    audio = np.mean(audio, axis=1)
    audio = np.trim_zeros(audio)
    audio = audio[:len(audio)-(len(audio)%rate)]
    rates = [ audio[i:i+rate] for i in range( 0, len(audio), rate ) ]
    return rates

def get_samples(paths, sec=1):
    samples = []
    for file_path in paths:
        rates = create_samples(file_path=file_path, sec=sec)
        if "ปกติ" in file_path:
            label = 0
        else:
            label = 1
        for frame in rates:
            samples.append( (frame, label) )
    shuffle(samples)
    return samples

samples = get_samples( train_paths, sec )
x_train = np.asarray( [sample[0] for sample in samples] ,dtype=np.float32)
x_train = np.tanh( x_train )
# x_train = np.tan( x_train )
y_train = keras.utils.to_categorical(np.asarray( [sample[1] for sample in samples] ), num_classes=2)


def get_logistic_model(input_dim):
    
    model = Sequential()
    
    model.add(Dense(256, input_dim=input_dim))
    model.add(Activation('linear'))
#     model.add(Dropout(0.5))
    model.add(Dense(128))
    model.add(Activation('linear'))
#     model.add(Dropout(0.5))
#     model.add(Dense(32))
#     model.add(Activation('linear'))
    model.add(Dropout(0.5))
    model.add(Dense(2))
    model.add(Activation('softmax'))
    
    sgd = SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])
    
    return model

model = get_logistic_model( x_train.shape[1] )
model.fit( x=x_train, y=y_train, epochs=50, batch_size=200 )

def evalualte(file_path, sec=1):
    print( "FILE: %s => " % file_path, end="" )
    rate, audio = wavfile.read( file_path )
    rate*=sec
    audio = np.mean(audio, axis=1)
    audio = np.trim_zeros(audio)
    audio = audio[:len(audio)-(len(audio)%rate)]
    rates = [ audio[i:i+rate] for i in range( 0, len(audio), rate ) ]

    x_test = np.asarray( [rate for rate in rates], dtype=np.float32 )
    x_test = np.tanh( x_test )
#     x_test = np.tan( x_test )

    label = 1
    if "ปกติ" in file_path:
        label = 0
    results = model.predict( x_test )
    count_label = 0
    for result in results:
        i = np.argmax(result)
        if i == label:
            count_label += 1
            
#         if i == 0:
#             print("ปกติ")
#         else:
#             print("เศร้า")
        
    count_wrong = len( x_test ) - count_label
    
    if count_wrong > count_label:
        print("WRONG")
        return 0
    if count_wrong == count_label:
        print("Do not know")
        return 0
    print("RIGHT")
    return 1

count = 0
shuffle(test_paths)
for path in test_paths:
    count += evalualte(path, sec)
s_acc = "%.2f" % (count / len(test_paths) * 100 )
#print( "Acc = %s %%" % s_acc )


model_folder = os.path.join( os.getcwd(), "Model" )
_, _, files = next( os.walk(model_folder) )

model_name = "Model_" + str(len(files)+1).zfill(4) + ".h5"
model.save( os.path.join( model_folder, model_name ) )
 
with open( 'log.txt', 'a' ) as logfile:
    logfile.write( "%s : %s\n" % (model_name, s_acc) )
    
create_samples(file_path, sec=1)





