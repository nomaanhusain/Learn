import os
import cv2
from PIL import Image
import numpy as np
import pickle
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(BASE_DIR,"images")

face_casscades= cv2.CascadeClassifier('casscades/data/haarcascade_frontalface_alt.xml')


print("############## Starting Training ......")
y_labels=[]
X_train=[]
id_count=0
labels_id={}

for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path=os.path.join(root,file)
            label=os.path.basename(root)
            print(label) 
            pil_image=Image.open(path).convert("L") #"L" converts to grayscale
            #size=(1000,1000)
            #final_img=pil_image.resize(size, Image.ANTIALIAS)
            
            image_arr=np.array(pil_image,"uint8")
            faces = face_casscades.detectMultiScale(image_arr, scaleFactor=2.5 ,minNeighbors=5)
            ##print(image_arr)
            ## labels_id dictonary is used to associate a number with a label ie name
            if not label in labels_id:
                labels_id[label]=id_count
                id_count+=1
            id_=labels_id[label]
            print(labels_id)
            
            for (x,y,w,h) in faces:
                roi =image_arr[y:y+h, x:x+w]
                X_train.append(roi)
                y_labels.append(id_)


##saving ids to a file with pickle

with open("labels.pickle",'wb') as f:
    pickle.dump(labels_id, f)


recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.train(X_train, np.array(y_labels))
recognizer.save("trainer.yml")
print("########### Training Complete ############3")