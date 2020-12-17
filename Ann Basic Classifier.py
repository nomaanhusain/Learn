#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers,models,datasets
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


(x_train,y_train), (x_test,y_test) = datasets.cifar10.load_data()


# In[3]:


y_train=y_train.reshape(-1,)
y_test=y_test.reshape(-1,)
y_train[:10]
types=["airplanes","car","bird","cat","deer","dog","frog","horse","ship","truck"]


# In[4]:


def plot_sample(x,y,index):
    plt.figure(figsize=(15,2)) #rezize for better viewing
    plt.imshow(x[index])
    plt.xlabel(types[y[index]])


# In[6]:


plot_sample(x_train,y_train,1154)


# In[7]:


x_train = x_train/255
x_test = x_test/255


# In[10]:


y_train_categorical = keras.utils.to_categorical(
    y_train, num_classes=10, dtype='float32'
)
y_test_categorical = keras.utils.to_categorical(
    y_test, num_classes=10, dtype='float32'
)


# In[15]:


ann = keras.Sequential([
        keras.layers.Flatten(input_shape=(32,32,3)),
        keras.layers.Dense(3000, activation='relu'),
        keras.layers.Dense(1000, activation='relu'),
        keras.layers.Dense(10, activation='sigmoid')    
    ])

ann.compile(optimizer='SGD',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


# In[16]:


ann.fit(x_train, y_train_categorical, epochs=11)


# In[18]:


ann.evaluate(x_test,y_test_categorical)


# In[ ]:




