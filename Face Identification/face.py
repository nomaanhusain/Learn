import numpy as np
import cv2
import pickle

face_casscades= cv2.CascadeClassifier('casscades/data/haarcascade_frontalface_alt2.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels={}
with open("labels.pickle",'rb') as f:
    oglabels = pickle.load(f)
    labels={v:k for k,v in oglabels.items()} #reverse key value pairs

cap = cv2.VideoCapture(0)
while (True):
    #capturing
    ret, frame=cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_casscades.detectMultiScale(gray, scaleFactor=2.5 ,minNeighbors=5)

    #showing region of intrest

    for (x,y,w,h) in faces:
        #print (x,y,w,h)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        cv2.imwrite("7.png", roi_color)

        id_,conf=recognizer.predict(roi_gray)
        if conf>=45 and conf<=100:
            #print(id_)
            #print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name=labels[id_]
            color=(100,175,100)
            stroke=1
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)


        #making rectangle
        color=(255,100,50) #bgr color of rec
        stroke=2 #bgr stroke of rec
        end_cord_x=x+w
        end_cord_y=y+h
        cv2.rectangle(frame,(x,y),(end_cord_x,end_cord_y),color,stroke)

    #displaying
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()