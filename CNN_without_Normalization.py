
# coding: utf-8

# In[1]:


import os

import cntk
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten, Conv1D, MaxPooling1D
from keras.optimizers import SGD

from scipy.io import wavfile
import numpy as np
from random import shuffle


# ## FRAMEWORK

# In[2]:


cntk.try_set_default_device( cntk.all_devices()[0] )


# ## DATA PREPARATION

# In[3]:


sec = 3

root, _dirs, files = next(os.walk( os.path.join( os.getcwd(), os.path.join( "dataset", "train" ))))
train_paths = [ os.path.join( root, file ) for file in files ]

root, _dirs, files = next(os.walk( os.path.join( os.getcwd(), os.path.join( "dataset", "test" ))))
test_paths = [ os.path.join( root, file ) for file in files ]


# In[4]:


def create_samples(file_path, sec=1):
    rate, audio = wavfile.read( file_path )
    rate *= sec
    audio = np.mean(audio, axis=1)
    audio = np.trim_zeros(audio)
    audio = audio[:len(audio)-(len(audio)%rate)]
    rates = [ audio[i:i+rate] for i in range( 0, len(audio), rate ) ]
    return rates


# In[5]:


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


# In[6]:


samples = get_samples( train_paths, sec )

x_train = np.asarray( [sample[0] for sample in samples] ,dtype=np.float32)
x_train = np.tanh(x_train)
x_train = x_train.reshape( x_train.shape[0], x_train.shape[1], 1 )

y_train = keras.utils.to_categorical(np.asarray( [sample[1] for sample in samples] ), num_classes=2)


# ## MODEL

# In[7]:


def get_model(input_dim):
    model = Sequential()
    
    model.add(Conv1D(filters=16, kernel_size=100, strides=2, activation="linear", input_shape=(input_dim,1)))
#     ---------------------------------------------------------------------------------------------
#    CONFIG MODEL
#     model.add(Conv1D(filters=8, kernel_size=100, strides=1, activation="linear"))
    
    
    
#     ---------------------------------------------------------------------------------------------   
    model.add(Flatten())
    model.add(Dense(10, activation='linear'))
    model.add(Dropout(0.5))
    model.add(Dense(2, activation='softmax'))
    
    sgd = SGD(lr=0.001, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])
    return model


# In[8]:


model = get_model( x_train.shape[1] )
model.fit( x=x_train, y=y_train, epochs=15, batch_size=100 )


# ## Evaluate

# In[9]:


def evalualte(file_path, sec=1):
    print( "FILE: %s => " % file_path , end="" )
    rate, audio = wavfile.read( file_path )
    rate*=sec
    audio = np.mean(audio, axis=1)
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
        print("WRONG")
        return 0
    print("RIGHT")
    return 1


# In[10]:


count = 0
for path in test_paths:
    count += evalualte(path, sec)
s_acc = "%.2f" % (count / len(test_paths) * 100 )
print( "Acc = %s %%" % s_acc )


# In[11]:


model_folder = os.path.join( os.getcwd(), "Model" )
_, _, files = next( os.walk(model_folder) )

model_name = "Model_" + str(len(files)+1).zfill(4) + ".h5"
model.save( os.path.join( model_folder, model_name ) )
 
with open( 'log.txt', 'a' ) as logfile:
    logfile.write( "%s : %s\n" % (model_name, s_acc) )

