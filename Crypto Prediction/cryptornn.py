import pandas as pd
import os
import numpy as np
import random
from sklearn import  preprocessing
from collections import deque
import time
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, BatchNormalization
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint


SEQ_LEN=60 ##see data from last 60 mins
PREDICT_TIME = 3 #Predict what would happen after 3 minutes
CRYPTO_TO_PRED="BCH-USD" #Which crypto to predict from
EPOCH=10
BATCH_SIZE=64
NAME=f"{SEQ_LEN}-SEQ-{CRYPTO_TO_PRED}-CURR-{int(time.time())}"
##Creating features for our model

def classify(current, future):
    if float(future)>float(current):
        return 1 #When more return 1, might be seen as a positive thing by the model
    else:
        return 0

#split data into x and y
def preprocessing_df(df):
    print("######## Preprocessing Started ##########")
    df.drop("future",1)
    for col in df.columns:
        if col != "target":
            df[col]=df[col].pct_change() #normalize
            df.dropna(inplace=True)
            df[col]=preprocessing.scale(df[col].values) #scale data between 0 to 1
    df.dropna(inplace=True)
    print("--- Building Sequential Data ---")
    sequential_data=[]
    prev_days=deque(maxlen=SEQ_LEN)
    for i in df.values:
        prev_days.append([n for n in i[:-1]])
        if len(prev_days) == SEQ_LEN:
            sequential_data.append([np.array(prev_days), i[-1]])
    random.shuffle(sequential_data)
    
    ##Balancing the buys and sells
    print("--- Balancing Buys and Sells ---")
    buys=[]
    sells=[]

    for seq,target in sequential_data:
        if target == 0:
            sells.append([seq , target])
        elif target == 1:
            buys.append([seq , target])
    random.shuffle(buys)
    random.shuffle(sells)

    lower = min(len(buys), len(sells))
    buys = buys[:lower]
    sells= sells[:lower]

    sequential_data=buys+sells
    random.shuffle(sequential_data)
    print("--- Split data ---")
    #Split data in x and y
    x=[]
    y=[]
    for seq,target in sequential_data:
        x.append(seq)
        y.append(target)

    return np.array(x), y


df = pd.read_csv("crypto_data/LTC-USD.csv",names=["time","low","high","open","close","volume"])
#print(df.head())
main_df=pd.DataFrame()
ratios=["BTC-USD","LTC-USD","ETH-USD","BCH-USD"]
for r in ratios:
    dataset=f"crypto_data/{r}.csv"
    df = pd.read_csv(dataset,names=["time","low","high","open","close","volume"])
    #print(df.head())
    df.rename(columns={"close": f"{r}_close", "volume" : f"{r}_volume"}, inplace=True)
    df.set_index("time",inplace=True)
    df=df[[f"{r}_close", f"{r}_volume"]]

    if len(main_df)==0:
        main_df = df
    else:
        main_df=main_df.join(df)
#print(main_df.head())
main_df['future']=main_df[f"{CRYPTO_TO_PRED}_close"].shift(-PREDICT_TIME) ##shit shifts up, so '-'
#print(main_df[[f"{CRYPTO_TO_PRED}_close", "future"]].head())

#Map calssify func in data

main_df['target']=list(map(classify , main_df[f"{CRYPTO_TO_PRED}_close"], main_df["future"])) 
#print(main_df[[f"{CRYPTO_TO_PRED}_close", "future", "target"]].head())

#Crearing chunks of data

times=sorted(main_df.index.values)
last_5pct=times[-int(0.05*len(times))]

#Split the data

validation_main_df=main_df[(main_df.index >= last_5pct)]
main_df=main_df[(main_df.index < last_5pct)]

train_x, train_y = preprocessing_df(main_df)

val_x, val_y = preprocessing_df(validation_main_df)

model = Sequential()
model.add(LSTM(128 , input_shape=(train_x.shape[1:]), return_sequences=True ))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(LSTM(128 , input_shape=(train_x.shape[1:]), return_sequences=True ))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(LSTM(128 , input_shape=(train_x.shape[1:])))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Dense(32 , activation="relu"))
model.add(Dropout(0.2))

opt = tf.keras.optimizers.Adam(lr=0.001, decay=1e-6)
model.compile(loss="sparse_categorical_crossentropy", optimizer=opt, metrics=["accuracy"])

tfBoard = TensorBoard(log_dir=f"logs/{NAME}")
print("####### Starting Training ########")
train_x = np.asarray(train_x)
train_y = np.asarray(train_y)
val_x = np.asarray(val_x)
val_y = np.asarray(val_y)
history = model.fit(train_x, train_y,batch_size=BATCH_SIZE,epochs=EPOCH,callbacks=[tfBoard],validation_data=(val_x,val_y))
